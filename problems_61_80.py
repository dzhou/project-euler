#!/usr/bin/env python
#

import sys
import os
import math
import time
import itertools 
from decimal import Decimal 

import mathlib as mlib


def problem61():
    def generate_triangle(n): return n*(n+1)/2
    def generate_square(n): return n**2
    def generate_pentagonal(n): return n*(3*n-1)/2
    def generate_hexagonal(n): return n*(2*n-1)
    def generate_heptagonal(n): return n*(5*n-3)/2
    def generate_octal(n): return n * (3*n-2)    
    octals = [generate_octal(n) for n in range(1, 4000)]
    octals = [str(n) for n in octals if n > 10**3 and n < 10**4]
    print octals

def problem76():
    sum_map = {}
    sum_map[1] = 1
    sum_map[2] = 1

    for n in range(3, 10):
        ways = 0
        for i in range(1, n):
            remain = n - i
            ways += sum_map[remain]
        sum_map[n] = ways

    for i in range(1, 10):
        print i, sum_map[i]


def problem75():

    triple_map = {}
    for i in range(2*10**6):
        triple_map[i] = 0

    for m in range(1, 10**5):
        n = m
        print m
        while True:
            a = (m**2-n**2)
            b = 2*m*n
            c = (m**2+n**2)
            triple_map[a+b+c] = 1
            if a+b+c > 2*10**6:
                break
            n += 1


        



def problem58():
    prime_map = mlib.prime_sieve(2*10**6)
    side_len = 3
    num_prime = 0.0
    num = 0

    while side_len < 20000:
        c = side_len**2
        corners = [n for n in range(c, c - side_len*3, -side_len+1)]
        num += len(corners)
        for p in corners:
            if p in prime_map:
                num_prime += 1
       
#        print num_prime, num
        if num_prime / num < 0.1:
            return side_len

        side_len += 2


def problem62():
    n = 10
    cube_map = {}
    cur_len = 4

    def check_permutation(cube_map):
        for cube in cube_map:
            cube_map[cube].sort()

        k = cube_map.keys()
        v = cube_map.values()
        vals = zip(v, k)
        vals.sort()

        for i in range(0, len(vals)-5):
            if (vals[i][0] == vals[i+1][0] and
                vals[i][0] == vals[i+2][0] and
                vals[i][0] == vals[i+3][0] and
                vals[i][0] == vals[i+4][0]):
                    return vals[i][1]

        return None

    while cur_len < 15:
        cube = n ** 3
        if len(str(cube)) != cur_len:
            k = check_permutation(cube_map)
            if k is not None:
                return k
            cube_map = {}
            cur_len += 1 

        cube_map[cube] = list(str(cube))
        n += 1

        

def problem67():
    f = open('files/p67_triangles', 'rb')
    data = f.readlines()
    f.close()
    
    grid = []
    for line in data:
        grid.append([int(n) for n in line.split(' ')])

    for i in range(len(grid)-2, -1, -1):
        for j in range(0, len(grid[i])):
            grid[i][j] += max(grid[i+1][j], grid[i+1][j+1])

    return grid[0][0]

def problem68():
    """
    Using the numbers 1 to 10, and depending on arrangements, it is possible 
    to form 16- and 17-digit strings. What is the maximum 16-digit string 
    for a "magic" 5-gon ring? 
    """
    max_str = ""
    for digits in itertools.permutations(range(1,11)):
        a,b,c,d,e,f,g,h,i,j = digits
        s = a+f+g 
        if (b+g+h == s and 
            i+h+c == s and 
            i+j+d == s and 
            f+j+e == s):
            gon = [(a,f,g),(b,g,h),(c,h,i),(d,i,j),(e,j,f)]
            min_digit = min(a,b,c,d,e)
            offset = [y for y in range(len(gon)) 
                if gon[y][0] == min_digit][0]
            ngon = gon[offset:] + gon[:offset]
            mstring = "".join([str(x1) for y1 in ngon for x1 in y1])
            if mstring > max_str:
                max_str = mstring 

    return max_str
    
    
def problem79():
    f = open('files/p79_keylogs', 'rb')
    data = f.readlines()
    f.close()
    
    key = []
    data.sort()
    order_map = {}
    num_set = set([])
    for i in range(0,10):
        order_map[str(i)] = []

    for line in data:
        line = line.strip()
        num_set |= set(line)
        order_map[line[0]].append(line[1])
        order_map[line[0]].append(line[2])
        order_map[line[1]].append(line[2])

    for n in order_map:
        order_map[n] = set(order_map[n])
        print n, order_map[n]

    changed = True
    while changed:
        changed = False
        for n in range(0, 10):
            for m in order_map[str(n)]:
                slen = len(order_map[str(n)])
                order_map[str(n)] -= order_map[m]
                if len(order_map[str(n)]) != slen:
                    changed = True
                    break

    key = []
    while len(order_map) > 0:
        for n in range(0, 10):
            if str(n) in order_map and len(order_map[str(n)] - set(key)) == 0:
                if str(n) in num_set:
                    key.append(str(n))
                del order_map[str(n)]
                break

    key.reverse()
    return ''.join(key)
    
        
    
def problem72():
    def totient(n):
        def loop(tot, pos):
            while pos>0:
                if mlib.gcd(pos,n)==1:  return loop(tot+1,pos-1)
                else:              return loop(tot,  pos-1)
            return tot  
        return loop(0,n-1) 


    for i in range(10000):
        totient(i)



def problem74():
    factorial_map = {}
    for n in range(10, 100):
        next_value = sum(mlib.factorial(int(c)) for c in str(n))     
        print next_value
    
    return 0





def problem63():
    """ 
    
    """
    count = 0
    # hardcoded limit
    for i in range(0, 1000):
        b = 1
        while True:
            p = b ** i
            if p < 10**i:
                b += 1
            else:
                break
            
            if p >= 10**(i-1):
                count += 1

    return count
    

    



def problem71():
    top = 3.0
    bot = 7.0
    fraclist = []
    while bot < 10**6:
        n = top/bot
        if n >= (3.0/7):
            bot += 1
        elif n <= (2.0/5):
            top += 1
        else:
            fraclist.append((n, top, bot))
            top += 1

    fraclist.sort()
    a,b = fraclist[-1][1:]
    return a / mlib.gcd(a,b)


def problem73():
    max = 1/2.0
    min = 1/3.0
    frac_map = {}
    for b in range(1, 10**4+1):
        for a in range(1, b):
            dec = float(a) / b
            if dec <= min or dec >= max:
                continue
            gcd = mlib.gcd(a, b)
            frac_map[(a/gcd, b/gcd)] = 1
        print b

    return len(frac_map)
   




def problem81():
    fin = open('files/p81_matrix')
    lines = fin.readlines()
    matrix = []
    for line in lines:
        row = [int(r) for r in line.split(',')]
        matrix.append(row)

    for i in range(1, 80):
        matrix[i][0] += matrix[i-1][0]
    for i in range(1, 80):
        matrix[0][i] += matrix[0][i-1]

    for y in range(1, 80):
        for x in range(1, 80):
            shortest_path = min(matrix[x-1][y], matrix[x][y-1])
            matrix[x][y] += shortest_path

    return matrix[-1][-1]




def problem66():
    sq_map = {}
    for i in range(1, 10**3):
        sq_map[i**2] = 1
    
    max_x = (0,0)

    for d in range(1, 100):
        if d in sq_map:
            continue
        print d
        x = 2
        while True:
            sq = (x-1)*(x+1)
            if sq % d == 0 and int(math.sqrt(sq/d))**2 == sq/d:
                if x > max_x[0]:
                    max_x = (x,d)
                break
            x += 1


    return max_x


def problem80():
    """
    It is well known that if the square root of a natural number is not an 
    integer, then it is irrational. The decimal expansion of such square 
    roots is infinite without any repeating pattern at all. 

    The square root of two is 1.41421356237309504880..., and the digital sum 
    of the first one hundred decimal digits is 475. 

    For the first one hundred natural numbers, find the total of the digital 
    sums of the first one hundred decimal digits for all the irrational 
    square roots. 
    """
    getcontext().prec = 200 
    digit_sum = 0
    for i in range(1, 100):
        s = str(Decimal(str(i)).sqrt())
        if s.find('.') >= 0:
            digits = str(s)[:101]
            digit_sum += sum([int(d) for d in digits if d != '.'])
    return digit_sum
        