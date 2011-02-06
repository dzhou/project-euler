import math
from fractions import Fraction


def problem323():
    """
    Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers
    (i.e. 0  yi  2^32, every value equally likely).

    For the sequence xi the following recursion is given:
    x0 = 0 and
    xi = xi-1 | yi-1, for i  0. ( | is the bitwise-OR operator)
    It can be seen that eventually there will be an index N such that 
        xi = 2^32 -1 (a bit-pattern of all ones) for all i  N.

    Find the expected value of N. 
    Give your answer rounded to 10 digits after the decimal point.
    """
    # k_n = expected steps for n-bits 
    # k_1 = 1/2 + 1/2(k_1+1)
    # k_2 = 1/4 + 1/2(k_1+1) + 1/4(k_2+1)
    # k_3 = 1/8 + 3/8(k_1+1) + 3/8(k_2+1) + 1/8(k_3+1)
    # ..

    #expected number of steps for n-bit
    esteps = [0] * 33

    #for binomial coefficients
    def pascal_generator():
        row = [1]
        while True:
            row = [1] + [row[i]+row[i+1] for i in range(0,len(row)-1)] + [1]
            yield row 

    pascal = pascal_generator()
    for level in range(1, 33):
        row = pascal.next()
        esteps[level] = (
            Fraction(2**level, 2**level-1) * 
            sum([Fraction(p,sum(row)) * (s+1) for p,s in zip(row,esteps)])
                )

    return round(float(esteps[32]), 10)

if __name__=="__main__":
    print problem323()

