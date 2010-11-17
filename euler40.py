#!/usr/bin/env python
#

import sys
import os
import math
import time
import copy

import mathlib as mlib


def problem21():
    """ 
    Let d(n) be defined as the sum of proper divisors of n (numbers less 
    than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a # b, then a and b are an amicable 
    pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 
    22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 
    are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    primelist = mlib.prime_sieve(10**4, output=[])
    amicable_map = {}
    am_sum = 0
    
    for i in range(1,10**4+1):
        factors = mlib.get_factors(i, primelist)
        amicable_map[i] = sum(factors[:-1])

    for i in amicable_map:
        if (amicable_map[i] != i and 
            amicable_map[i] in amicable_map and 
            amicable_map[amicable_map[i]] == i):
            am_sum += i
            
    return am_sum
    

def problem22():
    """ 
    Using names.txt (right click and 'Save Link/Target As...'), a 
    46K text file containing over five-thousand first names, begin by 
    sorting it into alphabetical order. Then working out the alphabetical 
    value for each name, multiply this value by its alphabetical 
    position in the list to obtain a name score.

    Forexample, when the list is sorted into alphabetical order, COLIN, 
    which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in 
    the list. So, COLIN would obtain a score of 938x 53 = 49714.

    What is the total of all the name scores in the file?
    """
    ASCII_OFFSET = 64

    f = open("files/p22_names", 'rb')
    data = f.readlines()
    f.close()
    
    names = data[0].replace('"', '').split(',')
    names.sort()
    sum = 0
    for i in range(0, len(names)): 
        nsum = 0
        for l in names[i]:
            nsum += ord(l)-ASCII_OFFSET
        sum += nsum*(i+1)
    
    return sum


#10 Sec
def problem23():
    """ 
    A perfect number is a number for which the sum of its proper divisors 
    is exactly equal to the number. For example, the sum of the proper 
    divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
    is a perfect number.

    A number whose proper divisors are less than the number is called deficient 
    and a number whose proper divisors exceed the number is called abundant.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
    number that can be written as the sum of two abundant numbers is 24. By 
    mathematical analysis, it can be shown that all integers greater than 28123 
    can be written as the sum of two abundant numbers. However, this upper limit 
    cannot be reduced any further by analysis even though it is known that the 
    greatest number that cannot be expressed as the sum of two abundant numbers
    is less than this limit.

    Find the sum of all the positive integers which cannot be written as 
    the sum of two abundant numbers.
    """
    primelist = mlib.prime_sieve(10**5, output=[])
    abundant = []
    
    for i in range(1, 28123+1):
        factors = mlib.get_factors(i, primelist)
        if sum(factors[:-1]) > i:
            abundant.append(i)
    
    ab_sum = {}
    ret_sum = 0
    for i in range(0, len(abundant)):
        if abundant[i] > 28123:
            break
        for j in range(0, len(abundant)):
            ab_sum[abundant[i]+abundant[j]] = 1
            if abundant[i]+abundant[j] > 28123:
                break

    for i in range(1, 28123+1):
        if i not in ab_sum:
            ret_sum += i
    return ret_sum        


def problem24():
    """ 
    A permutation is an ordered arrangement of objects. For example, 
    3124 is one possible permutation of the digits 1, 2, 3 and 4. If 
    all of the permutations are listed numerically or alphabetically, 
    we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits:
     0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    s = "0123456789"
    n = 10**6
    k = ""
    for x in range(9, -1, -1):
        for i in range(0, 10):
            if n > mlib.factorial(x):
                n -= mlib.factorial(x)
            else:
                k += s[i]
                s = s[:i] + s[i+1:]
                break

    return int(k)


def problem25():
    """ 
    The Fibonacci sequence is defined by the recurrence relation:
        F_(n) = F_(n-1) + F_(n-2), where F_(1) = 1 and F_(2) = 1.
    What is the first term in the Fibonacci sequence to contain 1000 digits?    
    F1 = 1
    F2 = 1
    F3 = 2
    """
    generator = mlib.fib()
    count = 1
    while True:
        n = generator.next()
        count += 1
        if len(str(n)) == 1000:
            return count
    

def problem26():
    """ 
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can 
    be seen that ^(1)/_(7) has a 6-digit recurring cycle.

    Find the value of d < 1000 for which ^(1)/_(d) contains the longest recurring 
    cycle in its decimal fraction part.    
    """
    def calc_repeating_frac(a, b):
        m = {}
        n = 0
        while True:
            if a < b:
                a *= 10
            a = a % b 
            if a in m:
                return n
            else:
                m[a] = n
            n += 1

    max_rp = (0,0)
    for i in range(1, 10**3):
        m = calc_repeating_frac(1,i)
        if m > max_rp[0]:
            max_rp = (m,i)

    return max_rp[1]
        
    
def problem27():
    """ 
    Euler published the remarkable quadratic formula:
    n^2 + n + 41

    It turns out that the formula will produce 40 primes for the consecutive 
    values n = 0 to 39. However, when n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 41 is 
    divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

    Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which 
    produces 80 primes for the consecutive values n = 0 to 79. The product of the 
    coefficients, -79 and 1601, is -126479.

    Considering quadratics of the form:
    n^2 + an + b, where |a| < 1000 and |b| < 1000     

    Find the product of the coefficients, a and b, for the quadratic expression 
    that produces the maximum number of primes for consecutive values of n, starting with n = 0.
    """
    prime_map = mlib.prime_sieve(1000**2, output={})
    max_chain = (0, 0, 0)

    #n**2 + a*n + b
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            n = 0
            chain = 0
            while True:
                p = (n + a)*n + b
                if p in prime_map:
                    chain += 1
                    n += 1
                else:
                    break
                            
            if chain > max_chain[0]:
                max_chain = (chain, a, b)
                #print max_chain
    
    return max_chain[1]*max_chain[2]
    
    
def problem28():
    """ 
    What is the sum of both diagonals in a 1001 by 1001 spiral 
    formed in the same way?
    """
    size = 1001
    ret = [1]
    ptr = 1
    step = 2
    
    while ptr < size**2:
        for i in range(0, 4):
            ptr += step
            ret.append(ptr)
        step += 2

    return sum(ret)


def problem29():
    """ 
    Consider all integer combinations of a^(b) for 2 # a # 5 and 2 # b # 5:
    2^(2)=4, 2^(3)=8, 2^(4)=16, 2^(5)=32
    3^(2)=9, 3^(3)=27, 3^(4)=81, 3^(5)=243
    4^(2)=16, 4^(3)=64, 4^(4)=256, 4^(5)=1024
    5^(2)=25, 5^(3)=125, 5^(4)=625, 5^(5)=3125

    If they are then placed in numerical order, with any repeats 
    removed, we get the following sequence of 15 distinct terms:
    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
    How many distinct terms are in the sequence generated by a^(b) 
    for 2 # a # 100 and 2 # b # 100?
    """
    d = {}
    for i in range(2, 101):
        for j in range(2, 101):
            if (i,j) not in d:
                d[(i,j)] = i**j
                d[(j,i)] = j**i

    res = d.values()
    res.sort()
    return len(set(res))


def problem30():
    """ 
    Surprisingly there are only three numbers that can be 
    written as the sum of fourth powers of their digits:
        1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
        8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
        9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)
    As 1 = 1^(4) is not a sum it is not included.
    The sum of these numbers is 1634 + 8208 + 9474 = 19316.
    Find the sum of all the numbers that can be written as 
    the sum of fifth powers of their digits.
    """
    fast_pow = {}
    for i in range(0, 10):
        fast_pow[i] = i**5

    total = 0
    digit = 2
    while True:
        digit += 1
        dmax = digit * fast_pow[9]
        if dmax < 10**(digit-1):
            break

    for n in range(10, dmax):
        if sum([fast_pow[int(d)] for d in str(n)]) == n:
            total += n

    return total
    
    
def problem31():
    """ 
    In England the currency is made up of pound and pence, p, and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, p1 (100p) and p2 (200p).
    
    It is possible to make p2 in the following way:
    1xp1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
        
    How many different ways can p2 be made using any number of coins?
    """
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    def calculate(cost, coins):
        total = 0
        for i in range(0, len(coins)):
            remain = cost - coins[i]
            if remain > 0:
                total += calculate(remain, coins[i:])
            elif remain == 0:
                total += 1

        return total

    return calculate(200, coins)


def problem32():
    """ 
    We shall say that an n-digit number is pandigital if it makes 
    use of all the digits 1 to n exactly once; for example, the 
    5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
    containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product 
    identity can be written as a 1 through 9 pandigital.    
    """
    res_map = {}
    i = 1
    j = 1
    while j < 10**4:
        while True:
            x = str(i*j) + str(i) + str(j)
            if mlib.is_pandigital(x):
                res_map[i*j] = 1

            if len(x) > 9:
                i = 1
                break
            i += 1

        j += 1

    return sum(res_map.keys())
    
    
def problem33():
    """ 
    The fraction ^(49)/_(98) is a curious fraction, as an inexperienced mathematician 
    in attempting to simplify it may incorrectly believe that ^(49)/_(98) = ^(4)/_(8), 
    which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less 
    than one in value, and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, 
    find the value of the denominator.
    """
    nr = 10
    dr = 10
    vals = []
    for i in range(10, 100):
        for j in range(i+1, 100):
            vals.append((i,j))  

    nr_sum = 1
    dr_sum = 1
    for pair in vals:
        (nr,dr) = pair
        if nr % 10 == 0 or dr % 10 == 0:
            continue
        if nr % 11 == 0 or dr % 11 == 0:
            continue        
        if str(nr)[1] == str(dr)[0]:
            if nr*(dr%10) == dr*(nr/10):
                nr_sum *= nr
                dr_sum *= dr
    
    return dr_sum / mlib.gcd(nr_sum, dr_sum)


def problem34():
    """ 
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    Find the sum of all numbers which are equal to the sum of the 
    factorial of their digits.
    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """
    fast_fac = {}
    for i in range(0, 10):
        fast_fac[i] = mlib.factorial(i)

    for i in range(10, fast_fac[9]*9):
        fast_fac[i] = fast_fac[i/10] + fast_fac[i%10]

    total = 0
    for n in range(10, fast_fac[9]*9):
        if fast_fac[n] == n:
            total += n
   
    return total


def problem35():
    """ 
    The number, 197, is called a circular prime because all rotations 
    of the digits: 197, 971, and 719, are themselves prime.
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 
    31, 37, 71, 73, 79, and 97.
    How many circular primes are there below one million?
    """
    count = 1
    for i in range(3, 1000000):
        m = str(i)
        not_prime = False
        for d in m:
            if int(d) % 2 == 0:
                not_prime = True
                break

        if not_prime:
            continue

        for i in range(0, len(m)):
            m = m[1:] + m[0]
            if not mlib.is_prime(int(m)):
                not_prime = True
                break
        
        if not not_prime:  
            count += 1
            
    return count


def problem36():
    """ 
    The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.
    Find the sum of all numbers, less than one million, which are palindromic in 
    base 10 and base 2.
    """
    max_len = len(str(int(mlib.int2bin(10**6))))
    psum = 0
    for i in xrange(0, 10**6):
        if mlib.is_palindrome(str(i)):
            b = int(mlib.int2bin(i, count=max_len))
            if mlib.is_palindrome(str(b)):
                psum += i

    return psum

    
def problem37():
    """ 
    The number 3797 has an interesting property. Being prime itself, it 
    is possible to continuously remove digits from left to right, and 
    remain prime at each stage: 3797, 797, 97, and 7. Similarly we can 
    work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from 
    left to right and right to left.    
    """
    count = 0
    n = 10
    sum = 0
    while count < 11:
        n += 1
        is_cprime = True
        
        for d in str(n):
            # 2 on the edge can be prime
            if d in "0468":
                is_cprime = False

        p = n  
        while p > 0:
            if not is_cprime or not mlib.is_prime(p):
                is_cprime = False
                break
            p /= 10

        p = n
        while p > 0: 
            if not is_cprime or not mlib.is_prime(p):
                is_cprime = False
                break
            p = p - int(str(p)[0]) * 10**(len(str(p))-1)
    
        if is_cprime:
            count += 1
            sum += n
    return sum


def problem38():
    """ 
    Take the number 192 and multiply it by each of 1, 2, and 3:
    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576
            
    By concatenating each product we get the 1 to 9 pandigital, 192384576. 
    We will call 192384576 the concatenated product of 192 and (1,2,3)
               
    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 
    4, and 5, giving the pandigital, 918273645, which is the concatenated 
    product of 9 and (1,2,3,4,5).
           
    What is the largest 1 to 9 pandigital 9-digit number that can be formed 
    as the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """
    # estimate max = 50000*1 + 50000*2 
    max = 50000
    max_pandigit = 0

    k = 0
    while k < max:
        k += 1
        n = 1
        while True:
            n += 1
            
            ret = [str(k*x) for x in range(1, n)]
            ret_j = ''.join(ret)
            if len(ret_j) > 9 and k > 0:
                break
            if mlib.is_pandigital(ret_j):
                if int(ret_j) > max_pandigit:
                    max_pandigit = int(ret_j)
                
    return max_pandigit


def problem39():
    """ 
    If p is the perimeter of a right angle triangle with integral length 
    sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p < 1000, is the number of solutions maximised?
    """
    def cmp_vals(a,b):
        return cmp(a[1], b[1])

    primeter_map = {}
    sq_map = {}
    sq_rev_map = {}

    for i in range(1, 1000):
        sq_rev_map[i**2] = i
        sq_map[i] = i**2
        primeter_map[i] = 0

    for a in range(1, 1000):
        for b in range(1, 1000):
            if a + b > 500:
                break
            c2 = sq_map[a] + sq_map[b]
            if c2 in sq_rev_map:
                if sq_rev_map[c2] + a + b < 1000:
                    primeter_map[a+b+sq_rev_map[c2]] += 1

    countlist = primeter_map.items()
    countlist.sort(cmp_vals)
    return countlist[-1][0]
    

def problem40():
    """ 
    An irrational decimal fraction is created by concatenating the positive integers:
    0.123456789101112131415161718192021...
    It can be seen that the 12^(th) digit of the fractional part is 1.
    If d_(n) represents the n^(th) digit of the fractional part, find the value of the following expression.
    d_(1) x d_(10) x d_(100) x d_(1000) x d_(10000) x d_(100000) x d_(1000000 
    """
    count = 0
    d = 1
    prod = 1
    for i in range(1, 1000000):
        count += len(str(i))
        index = 10 ** d
        if count > index:
            d += 1
            prod *= int(str(i)[index-count-1])
    return prod
