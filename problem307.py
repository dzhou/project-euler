"""
k defects are randomly distributed amongst n integrated-circuit chips 
produced by a factory (any number of defects may be found on a chip 
and each defect is independent of the other defects).

Let p(k,n) represent the probability that there is a chip with at least 3 defects.
For instance p(3,7)  0.0204081633.

Find p(20 000, 1 000 000) and give your answer rounded to 10 decimal 
places in the form 0.abcdefghij
"""
import math
import itertools
import operator
from decimal import Decimal


def fac(n, k=2):
    if n == 0:
        return 1 
    return reduce(operator.mul, range(k, n+1))


def problem307():    
    k = 10**6
    n = 10**4
    d = 10**4

    last_d = 1 
    res = [fac(k, k-n+1) * fac(20000) / 2**d / fac(n-d) / fac(d)#]

    for i in range(10**4-1):
        b = res[-1]*2*(20000-n)*(k-n) / last_d / (last_d+1)
        res.append(b)
        n += 1 
        last_d += 2 
    
    s = reduce(operator.add, res)
    return Decimal(1) - Decimal(s) / Decimal((10**6)**20000)
