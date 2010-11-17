import sys
import os
import math

import mathlib as mlib


def problem102():
    fin = open('files/p102_triangles')
    lines = fin.readlines()
    triangles = []
    for line in lines:
        triangles.append([int(r) for r in line.split(',')])
    
    count = 0
    for triangle in triangles:
        x1, y1, x2, y2, x3, y3 = triangle
        area = abs(x1*y2+x2*y3+x3*y1-x1*y3-x3*y2-x2*y1)/2.0
        a1 = abs(0*y2+x2*y3+x3*0-0*y3-x3*y2-x2*0)/2.0
        a2 = abs(x1*0+0*y3+x3*y1-x1*y3-x3*0-0*y1)/2.0
        a3 = abs(x1*y2+x2*0+0*y1-x1*0-0*y2-x2*y1)/2.0

        if area == a1+a2+a3:
            count += 1

    return count


def problem104():
    f_n1 = f_n2 = 1
    k = 2
    a = []
    while True:
        k += 1
        #n = (f_n1 + f_n2) % 10**9
        n = (f_n1 + f_n2)
        f_n1 = f_n2
        f_n2 = n


        if mlib.is_pandigital(str(n)[:9]):
            print k
            a.append(k)

            if k > 20000:
                break
    print "-"*80
    for i in range(1, len(a)):
        print a[i] - a[i-1]
        #if mlib.is_pandigital(str(n)):
        #    print k, n
            #fibn = str(mlib.get_fibn(k))[:9]
            #if mlib.is_pandigital(fibn):
            #    return k


