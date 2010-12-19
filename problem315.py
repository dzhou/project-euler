"""
Sam and Max are asked to transform two digital clocks into two "digital 
root" clocks. A digital root clock is a digital clock that calculates 
digital roots step by step. 

When a clock is fed a number, it will show it and then it will start the 
calculation, showing all the intermediate values until it gets to the 
result. For example, if the clock is fed the number 137, it will show: 
"137" "11" "2" and then it will go black, waiting for the next number. 

Every digital number consists of some light segments: three horizontal 
(top, middle, bottom) and four vertical (top-left, top-right, 
bottom-left, bottom-right). Number "1" is made of vertical top-right and 
bottom-right, number "4" is made by middle horizontal and vertical  top-left, 
top-right and bottom-right. Number "8" lights them all. 

The clocks consume energy only when segments are turned on/off. To turn 
on a "2" will cost 5 transitions, while a "7" will cost only 4 
transitions. 

Sam and Max built two different clocks. Sam's clock is fed e.g. number 
137: the clock shows "137", then the panel is turned off, then the next 
number ("11") is turned on, then the panel is turned off again and 
finally the last number ("2") is turned on and, after some time, off. 

Max's clock works differently. Instead of turning off the whole panel, 
it is smart enough to turn off only those segments that won't be needed 
for the next number. Of course, Max's clock consumes less power than 
Sam's one. The two clocks are fed all the prime numbers between A = 10^7 
and B = 2*10^7. Find the difference between the total number of 
transitions needed by Sam's clock and that needed by Max's 
"""

from number_theory import *
from mathlib import *
import itertools 

# use bitarray to represent on/off segments
digits = {
    0: [1,1,1,0,1,1,1],
    1: [0,0,0,0,0,1,1],
    2: [0,1,1,1,1,1,0],
    3: [0,0,1,1,1,1,1],
    4: [1,0,0,1,0,1,1],
    5: [1,0,1,1,1,0,1],
    6: [1,1,1,1,1,0,1],
    7: [1,0,1,0,0,1,1],
    8: [1,1,1,1,1,1,1],
    9: [1,0,1,1,1,1,1],
}


def problem315():
    # cost difference for digit -> digit transition 
    transition_map = {}
    for n,m in itertools.product(range(10), repeat=2):
        ns = digits[n]
        ms = digits[m]
        shared = sum([1 for x in range(len(ns)) if ns[x] == 1 and ms[x] == 1])
        player_sam = sum(ns) + sum(ms)
        player_max = player_sam - shared*2
        transition_map[(str(n),str(m))] = player_sam - player_max

    # all 2 digits -> 2 digits transitions 
    for n in itertools.product(range(10), repeat=2):
        for m in itertools.product(range(10), repeat=2):
            n = "".join(map(str, n))
            m = "".join(map(str, m))
            cost = sum([transition_map[x] for x in zip(n,m)])
            transition_map[n,m] = cost 

    # calculate !
    cost = 0
    primes = [p for p in prime_sieve(2*10**7, []) if p > 10**7]
    for prime in primes:
        root = prime 
        while root >= 10:
            root2 = get_digit_root(root) 
            size2 = len(str(root2)) 
            key = (str(root)[-size2:], str(root2))
            cost += transition_map[key] 
            #print root, root2, transition_map[key]
            root = root2 
            
    return cost 


