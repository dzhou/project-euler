"""
Project Euler 312 

- A Sierpinski graph of order-1 (S1) is an equilateral triangle.
- Sn+1 is obtained from Sn by positioning three copies of Sn so that every pair of copies has one common corner.

Let C(n) be the number of cycles that pass exactly once through all the vertices of Sn.
For example, C(3) = 8 because eight such cycles can be drawn on S3, as shown below:

It can also be verified that :
C(1) = C(2) = 1
C(5) = 71328803586048
C(10 000) mod 108 = 37652224
C(10 000) mod 138 = 617720485
Find C(C(C(10 000))) mod 138.

I worked out most of the problem with pen/paper
iterative formula: 
    k(1) = 1
    k(n+1)= 3*[k(n-1)**3]
    C(n) = k(n)**3
    
and cycle lenth of C is 28960854
"""

def find_cycle(mod=13**8):
    k = 24 
    c = 0
    while True:
        k = 3*(k**3) % mod 
        c += 1
        if k == 24:
            break 
    return c    


# function C for n >= 5
def C(n, mod):
    k = 24
    c -= 4
    while c > 0:
        c -= 1 
        k = 3*(k**3) % m
    return k**3 % m


def problem312():
    return C(C(C(10**4, 28960854), 28960854), 13**8)
