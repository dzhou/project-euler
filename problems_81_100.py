import sys
import os
import math
import itertools 

import mathlib as mlib
from mathlib import *

def problem85():
    """
    By counting carefully it can be seen that a rectangular grid 
    measuring 3 by 2 contains eighteen rectangles:
    Although there exists no rectangular grid that contains exactly two 
    million rectangles, find the area of the grid with the nearest solution.
    """
    # number of recs in NxM == (recs in 1xN) * (recs in 1xM)
    # generate list: [number of rectangles in 1xN grid]
    row = 2
    rectangle_count = [(1,1)]
    while rectangle_count[-1][1] < 2*10**6:
        last_row, last_count = rectangle_count[-1]
        rectangle_count.append((row, last_count + row))
        row += 1

    # linear function to find the minimum grid
    head = 0
    tail = len(rectangle_count)-1
    min_difference = 2*10**6
    grid_area = 0
    while head < tail:
        total = rectangle_count[head][1] * rectangle_count[tail][1]
        difference = 2*10**6 - total
        
        if abs(difference) < min_difference:
            min_difference = abs(difference)
            grid_area = rectangle_count[head][0] * rectangle_count[tail][0] 

        if difference > 0:
            head += 1
        else:
            tail -= 1

    return grid_area


def problem86():
    # For AxBxC cube, the paths are given by
    # (a**2 + (b+c)**2) ** 1/2 
    
    pass


def problem90():
    rules = [(0,1), (0,4), (0,9),
        (1,6), (2,5), (3,6), (4,9),
        (4,6), (8,1)]
    
    def satisfy_rules(s1, s2):
        for x,y in rules:
            if y == 6 or y == 9:
                if not (((6 in s1 or 9 in s1) and x in s2)
                    or ((6 in s2 or 9 in s2) and x in s1)):
                    return False
            elif not ((x in s1 and y in s2)
                or (y in s1 and x in s2)):
                return False 
        return True 

    count = 0
    for s1 in itertools.combinations(range(10), 6):
        for s2 in itertools.combinations(range(10), 6):
            if satisfy_rules(s1, s2):
                count += 1
    return count / 2


def problem92():
    
    def run_chain(n, cmap):
        if n in cmap:
            return cmap[n]
        else:
            m = n
            dsum = 0
            while n > 0:
                dsum += (n % 10)**2
                n /= 10            
            cmap[m] = run_chain(dsum, cmap)
            return cmap[m]
    
    count = 0
    chain_map = {1:0, 89:1}
    for i in range(1, 100):
        count += run_chain(i, chain_map)
    
    # generate up to 9**2*6
    for i in range(100, 600):
        run_chain(i, chain_map)

    for n in xrange(1, 10**5):
        dsum = 0
        while n > 0:
            dsum += (n % 10)**2
            n /= 10 
            
        for x in range(0, 10):
            for y in range(0, 10):
                count += chain_map[dsum+x**2+y**2]

    return count    
    

def problem97():
    #28433x2^(7830457)
    m = 2**1000
    x = 2**457 * 28433
    
    for i in xrange(0, 7830):
        x *= m
        x %= 10**10 

    return x+1


def problem99():
    """ 
    Using base_exp.txt (right click and 'Save Link/Target As...'), a 
    22K text file containing one thousand lines with a base/exponent 
    pair on each line, determine which line number has the greatest numerical value.    
    """
    def cmp_exp(a,b):
        return cmp(math.log(a[0],10)*a[1], math.log(b[0],10)*b[1])

    f = open('files/p99_base_exp', 'rb')
    data = f.readlines()
    f.close()

    # exp=[base, exponent, line_number]
    exps = []
    for i in range(0,len(data)):
        (n1,n2) = data[i].strip().split(',')
        exps.append((int(n1),int(n2),i+1))

    exps.sort(cmp_exp)
    return exps[-1][2]


def problem100():
    blue = 15
    red = 6
    max = 10**10
    res = []
    while True:
        total = blue + red
        u = total*(total-1)
        l = blue**2-blue
        
        if u % l == 0 and u/l == 2:
            print blue, red, blue+red
            res.append((blue, red))
            if len(res) == 4:
                break

        if u / l < 2:
            red += 1
        else:
            blue += 1

    for i in range(1, len(res)):
        b1, r1 = res[i]
        b2, r2 = res[i-1]
        print float(b1+r1) / (b2+r2)

    s = 803761
    m = 5.82840961820
    p = 1
    while True:
        n = s * m**p
        if n > 10**12:
            print s, m, p, n, int(n)
            break
        p += 1

    s = 1070379110495
    for i in range(0, 10**8):
        np = s + i
        nn = s - i

        bp = np * (np-1)
        bn = nn * (nn-1)

        h1 = int(math.sqrt(bp/2))
        h2 = int(math.sqrt(bn/2))
        
        if h1 * (h1+1) * 2 == bp:
            print "total:", np
            print "blue:", h1+1
            return h1+1    