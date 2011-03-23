import math
import mathlib
from decorators import memoized
from fractions import Fraction, gcd



def problem329():
    """
    Susan has a prime frog.
    Her frog is jumping around over 500 squares numbered 1 to 500. He can only
    jump one square to the left or to the right, with equal probability, and he
    cannot jump outside the range [1;500].
    (if it lands at either end, it automatically jumps to the only available
    square on the next move.)

    When he is on a square with a prime number on it, he croaks 'P' (PRIME) with
    probability 2/3 or 'N' (NOT PRIME) with probability 1/3 just before jumping
    to the next square. 
    When he is on a square with a number on it that is not a prime he croaks 'P'
    with probability 1/3 or 'N' with probability 2/3 just before jumping to the
    next square.

    Given that the frog's starting position is random with the same probability
    for every square, and given that she listens to his first 15 croaks, what is
    the probability that she hears the sequence PPPPNNPPPNPPNPN? 
    Give your answer as a fraction p/q in reduced form.
    """
    seq = "PPPPNNPPPNPPNPN"
    primes = mathlib.prime_sieve(500)
    
    @memoized
    def f(k, seq):
        curr, rest_seq = seq[0], seq[1:]
        if k in primes:
            p = Fraction(2,3) if curr == 'P' else Fraction(1,3)
        else:
            p = Fraction(2,3) if curr == 'N' else Fraction(1,3)

        if len(rest_seq) == 0:
            return p
        elif k == 1:
            return p * f(2, rest_seq)
        elif k == 500:
            return p * f(499, rest_seq)
        else:
            return p * (f(k-1, rest_seq) + f(k+1, rest_seq)) / 2

    return sum(f(i, seq) for i in range(1,501)) / 500



if __name__=="__main__":
    print problem329()
