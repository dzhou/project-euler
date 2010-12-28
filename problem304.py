import math
import sys 
from number_theory import *
from sequences import fibonacci_matrix


def problem304():
    """
    For any positive integer n the function next_prime(n) returns the 
    smallest prime p such that pn. 

    The sequence a(n) is defined by: a(1)=next_prime(1014) and 
    a(n)=next_prime(a(n-1)) for n1. 

    The fibonacci sequence f(n) is defined by: f(0)=0, f(1)=1 and 
    f(n)=f(n-1)+f(n-2) for n1. 
    The sequence b(n) is defined as f(a(n)). 
    Find b(n) for 1n100 000. Give your answer mod 1234567891011.    
    """
    
    # !! super slow brute-force 
    # but the log-n fibonacci generator is cool though ..
    c = 10**14 + 1 
    m = 1234567891011
    prime_count = 0
    fibsum = 0     
    
    while prime_count < 10**5:
        if miller_rabin(c):
            prime_count += 1 
            fibsum = (fibsum + fibonacci_matrix(c, m)) % m 

        c += 2            
    return fibsum % m 


