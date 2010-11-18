#!/usr/bin/env python
#
# Kefei Dan Zhou
#

import math
import time


def is_palindrome(s):
    """
    @type s: indexable object, typically string or list
    @param s: check if s is palindrome
    """
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


def is_prime(n):
    """
    @type n: integer
    @param n: check if n is prime
    """
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False

    r = int(math.floor(math.sqrt(n)))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6

    return True


def is_pandigital(n, m=9):
    """
    n is m-digit pandigital iff digits [1-m] occurs in n exactly once
    @type n: int
    @param n: check if its pandigital
    @type m: int (1-9)
    @param m: number of digits
    """
    if len(str(n)) != m:
        return False

    for d in "1234567890"[:m]:
        if d not in str(n):
            return False

    return True


def fib():
    i = 0
    j = 1
    while True:
        j = i + j
        i = j - i
        yield j


def timed_trial(func, debug=True):
    t1 = time.time()
    out = func()
    t2 = time.time()
    if debug:
        print "solution:", out
        print "completed:", t2-t1, "seconds"
    return (out, t2-t1)    


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

"""
def safe_div(a,b):
    if b == 0:
        return 0
    else:
        return a/b
"""
"""
def get_factors(a):
    div = 2
    factors = []
    while a > 1:
        while a % div == 0:
            factors.append(div)
            a /= div
        div += 1

    return factors
"""

def depracated__isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n%x == 0:
            return False
    return True


def gen_permutation(str):
    if len(str) <=1:
        yield str
    else:
        for perm in gen_permutation(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


def count_permutations(items):
    return factorial(len(items))


def gen_prime(start=2):
    p = start

    while True:
        while not isprime(p):
            p += 1
        yield p


def factorial(n):
    m = 1
    while n > 1:
        m *= n
        n -= 1
    return m


def int2bin(n, count=24):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])


def prime_sieve_1(max, output_type, prime_only=True):
    sieve = range(0, max)
    sieve[1] = 0

    for i in range(2, int(math.sqrt(max))):
        if i%2==0 or not isprime(i):
            continue
        k = i*2
        while k < len(sieve):
            sieve[k] = 0
            k += i

    pmap = {}
    for k in range(0, max):
        if sieve[k] == 0 and not prime_only:
            pmap[k] = False
        elif sieve[k] > 0:
            pmap[k] = True
        else:
            pass
    
    if type(output_type) == dict:
        return pmap
    elif type(output_type) == list and prime_only:
        return pmap.keys()
    else:
        return sieve


def prime_sieve(n, output={}):
    nroot = int(math.sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    if type(output) == dict:
        pmap = {}
        for x in sieve:
            if x != 0:
                pmap[x] = True
        return pmap
    elif type(output) == list:
        return [x for x in sieve if x != 0]
    else:
        return None




def reverse_number(n):
    """
    @type n: int
    @param n: integer to reverse
    """
    rnum = 0
    digit = 0
    while n > 0:
        rnum *= 10
        digit = n % 10
        rnum += digit
        n /= 10

    return rnum    
    

def get_prime_factors(n, primelist):
    fs = []
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            fs.append((p, count))

    return fs


def get_factors(n, primelist=None):
    if primelist is None:
        primelist = prime_sieve(n,output=[])

    fcount = {}
    for p in primelist:
        if p > n:
            break
        if n % p == 0:
            fcount[p] = 0
    
        while n % p == 0:
            n /= p
            fcount[p] += 1

    factors = [1]
    for i in fcount:
        level = []
        exp = [i**(x+1) for x in range(fcount[i])]
        for j in exp:
            level.extend([j*x for x in factors])
        factors.extend(level)

    return factors


def get_any_factor(n, primelist):
    for p in primelist:
        if n % p == 0:
            return n/p

    return None


def gen_combinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in gen_combinations(items[i+1:],n-1):
                yield [items[i]]+cc

phi = (1 + 5**0.5) / 2
def get_fibn(n):
    return int(round((phi**n - (1-phi)**n) / 5**0.5))
