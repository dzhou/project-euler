#!/usr/bin/env python
#

import sys
import os
import math
import time

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


def problem187():
    # sloan's A066265
    return 17427258


def problem121():
    def calculate_level(turn, n):
        total = 0
        gen = mlib.gen_combinations(range(1,turn), n)
        try:
            while True:
                total += reduce(lambda x, y: x*y, gen.next())
        except StopIteration:
            pass

        return total

    turns = 15
    wins = 1
    for i in range(1, (turns-1)/2+1):
        wins += calculate_level(turns+1, i)
    
    return mlib.factorial(turns+1) / wins

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


def problem124():
    """
    def gen_multipliers(numbers, factors, max):
        multipliers = []
        i = 1
        while True:
            m = factors[0]**i
            if m > max:
                break
            multipliers.append(m)
            i += 1

        return multipliers 

    max = 10**5
    for n in range(2, 10):
        ms = gen_multipliers([], [n], max)
        print len(ms)
    """
    rad_map = {}
    for i in range(1, 10**5):
        rad_map[i] = i

    prime_list = mlib.prime_sieve(10**5, [])
    for p in prime_list:
        r = p*p
        while r*p < len(rad_map):
            rad_map[r*p] /= r
            r *= p

    for i in range(1, 100):
        print i, rad_map[i]
    return 0


def problem91():
    points = []
    for x in range(0, 51):
        for y in range(0, 51):
            points.append((x,y))
   
    for p1 in points:
        for p2 in points:
            pass


def problem69():
    #def totient(n):
    #    return sum([1 for i in range(1,n) if mlib.gcd(i,n)==1])
    """
    max = 10**6
    prime_map = mlib.prime_sieve(max+1) 
    prime_list = prime_map.keys()
    prime_list.sort()
    totient_map = {}

    for p in prime_map:
        totient_map[p] = p-1
        base = p*p
        while base < max+1:
            totient_map[base] = totient_map[base/p] * p
            base *= p

    for n in range(2, max+1):
        if n not in totient_map:
            reduced = mlib.get_any_factor(n, prime_list)
            totient_map[n] = totient_map[reduced] * totient_map[n/reduced]
 
    print totient_map[10]
    print totient_map[100]
    return sum(totient_map.values())
    """
    pass

def problem205():
    peter_dice = {}
    for i in range(0, 9):
        pass

    def gen_dice_roll(num_face, num_roll):
        dices = [1 for i in range(num_face)]
        
        while True:
            dices = None
        



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






def problem213():
    pass
    import random

    grid = [[0 for i in range(0,30)] for j in range(0,30)]


        

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



def problem148():
    
    def print_pascal(n, debug=True):
        row = [1]
        count = 0
        for i in range(0, n):
            if debug:
                print i+1, row
            for i in row:
                if i % 7 == 0:
                    count += 1
            r = [1]
            for i in range(0, len(row)-1):
                r.append((row[i]+row[i+1])%7)
            r.append(1)
            row = r
        return count

    """
    end_row = 100
    print 'correct', print_pascal(end_row)

    sum = 0
    for i in range(7, end_row-(end_row%7), 7):
        print i, "+", (i/7-1)*21
        sum += (i / 7) * 21
        pass

    for i in range(end_row-(end_row%7), end_row):
        print i,'+',(i/7)*(6-i%7)
        sum += (i/7)*(6-i%7)
    
    print sum
    #sum = (end_row+1)*end_row/2 - sum
    return sum
    """
    
    prime_map = prime_sieve(10*10**6, output={})
    print len(prime_map)
    
    max_n = int(math.sqrt(150*10**6)) + 27
    #max_n = 150 * 10**6
    max_n = 100
    #for n in range(10, max_n):
    n = 2
    while n < max_n:
        n += 2
        n2 = n**2
        if (isprime(n2+1) and isprime(n2+3) and isprime(n2+7) and
            isprime(n2+9) and isprime(n2+13) and isprime(n2+27)):
            print n
        if n % 1000==0:
            print n    


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



def problem160():
    
    trail = {}
    
    c = 1
    for i in range(1, (10**4)):
        #if i % 1000 == 0:
            #print i
        if i%100000 != 0:
            c *= (i%100000)
        while c % 10 == 0:
            c /= 10
        c = c%100000
    
    print str(c)[-10:]

    k = 1
    for i in range(1, 100):
        k *= i
    print k

    #for i in range(1000000, 1000150):
        #print i%100000
        #n = i
        #while n%10 == 0:
            #n /= 10
        #print n
    #for i in range(0, 10**10):
    #i = 1
    #max = 10**10
    ##while i < max:
        #if i % 10**6 == 0:
            #print i
        #i += 1
        #pass

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
    

def problem97():
    """
    28433x2^(7830457)+1
    """
    
    i = 2
    c = 2
    two_map = {1:1}
    while i <= 7830457:
        c = c ** 2
        c %= 10**10
        two_map[i] = c
        i = i * 2
    
    power = int2bin(7830457, count=32)
    end_sum = 1
    for n in range(0, len(power)):
        print power[n], 2**(len(power)-n-1)
        if int(power[n]) == 1:
            end_sum *= two_map[2**(len(power)-n-1)]
            #print "ADD", end_sum

    return str(end_sum * 28433 + 1)[-10:]
    

    

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
   
def problem173():

    def get_max_edge(start_edge, max_tiles):
        tiles = (start_edge - 1) * 4
        edge = start_edge
        while tiles < max_tiles:
            edge += 1
            tiles += (edge - 1) * 4

        return edge

    
    hole_edge = 1
    total = 0
    while True:
        start_edge = hole_edge + 2
        max_edge = get_max_edge(start_edge, 100)
        sq_num = (max_edge - start_edge) / 2 + 1
        print start_edge, max_edge, sq_num
        if sq_num <= 0:
            break
        else:
            total += sq_num
            hole_edge += 1

    return total


def problem206():
    #p = 1020304050607080900
    max_p = 1929394959697989990
    min_p = 1020304050607080900

    max_n = int(math.sqrt(max_p))/100
    min_n = int(math.sqrt(min_p))/100

    i = min_n
    while i < max_n:
        n1 = i * 100 + 30
        n2 = i * 100 + 70
        k1 = str(n1**2)
        k2 = str(n2**2)
    
        if k1[2] == '2' and k1[4] == '3' and k1[6] == '4' and k1[8] == '5':
            if k1[10] == '6' and k1[12] == '7' and k1[14] == '8' and k1[16] == '9':
                return n1
        if k2[2] == '2' and k2[4] == '3' and k2[6] == '4' and k2[8] == '5':
            if k2[10] == '6' and k2[12] == '7' and k2[14] == '8' and k2[16] == '9':
                return n2
        
        i += 1


def problem145():
    pass
    i = 0
    while i < 10**9:
        i += 1


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


def problem97():
    #28433x2^(7830457)
    m = 2**1000
    x = 2**457 * 28433
    
    for i in xrange(0, 7830):
        x *= m
        x %= 10**10 

    return x+1


"""
def problem62():
    # permutation inclde leading zero
    # fuck up results
    cube_map = {}
    for i in range(0, 10**5):
        cube_map[i**3] = 1

    max = (10**5)**3
    i = 1
    while i < 10**3:
        print i,i**3
        i += 1
        g = mlib.gen_permutation(str(i**3))
        count = 0
        try:
            while True:
                if int(g.next()) in cube_map:
                    #print "IN"
                    count += 1
        except:
            pass

        if count > 5:
            return i
"""

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


def problem104():
    fib_n1 = 1
    fib_n2 = 1
    div = 10**9
    n = 1
    #m = 1
    #a1 = 1
    #a2 = 1
    phi = (1 + math.sqrt(5)) / 2
    r5 = math.sqrt(5)
    #fib_map = {1:(1,0), 2:(0,1)}    
    #for i in range(1, 99):
        #fib_map[i+2] = (fib_map[i][0]+fib_map[i+1][0], fib_map[i][1]+fib_map[i+1][1])
            
    m = {}
    p = phi
    m[0] = p
    #for i in range(1, 20*10**6):
    for i in range(1, 4000):
        #m[i] = int(m[i-1]*phi * (div*10) % div)
        if i == 2748:
            print m[i]
        if mlib.is_pandigital(m[i]):
            print i
        
    print "DONE"
    while True:
        n += 1
        f = (fib_n1 + fib_n2) % div        
        if n % 10000 == 0:
            print n
           
        if mlib.is_pandigital(str(f)[-9:]):
            if mlib.is_pandigital(m[n+1]):
                return n+1
            #print n+1
            #print phi, n+1
            #print #math.log(phi**(n+1)/r5, 10)
            #if mlib.is_pandigital(s):
                #print s, n+1
                #return n+1

        fib_n1 = fib_n2
        fib_n2 = f


    """    
    return
    m = {}
    last_p = 0
    while n < 10**9:
        n += 1
        f = (fib_n1 + fib_n2) % div
        
        if mlib.is_pandigital(str(f)[-9:]):
            m = n+1
            a1 = 1
            a2 = 1
            while m > (len(fib_map)-2):
                m -= (len(fib_map)-2)
                a1_t = a1
                a1 = fib_map[99999][0]*a1 + fib_map[99999][1]*a2
                a2 = fib_map[100000][0]*a1_t + fib_map[100000][1]*a2

            a = fib_map[m][0]*a1 + fib_map[m][1]*a2
            print n+1, str(a)[-9:]
            if mlib.is_pandigital(str(a)[:9]):
                return len(str(a)), a[:9]
        fib_n1 = fib_n2
        fib_n2 = f
    """
