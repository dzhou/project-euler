import sys
import os
import math
import itertools 

import mathlib as mlib

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



def problem54():

    def same_suits(hand):
        return (hand[0][1] == hand[1][1] == 
                hand[2][1] == hand[3][1] == hand[4][1])

    def card2num(hand):
        for i in range(0, 5):
            if hand[i][0] == 'T':
                hand[i] = 10
            elif hand[i][0] == 'J':
                hand[i] == 11
            elif hand[i][0] == 'Q':
                hand[i] == 12
            elif hand[i][0] == 'K':
                hand[i] == 13
            elif hand[i][0] == 'A':
                hand[i] == 1
            else:
                hand[i] = int(hand[i][0])
        return hand

    player1 = []
    player2 = []

    fin = open('files/p54_poker')
    data = fin.readlines()
    for line in data:
        hand1 = line[:15].split()
        hand2 = line[15:].split()

        hand1.append(same_suits(hand1))
        hand2.append(same_suits(hand2))
        
        print card2num(hand1)

        
        
    """ Each of the six faces on a cube has a different digit (0 to 9) 
    written on it; the same is done to a second cube. By placing the two 
    cubes side-by-side in different positions we can form a variety of 
    2-digit numbers. 

    For example, the square number 64 could be formed: 

    In fact, by carefully choosing the digits on both cubes it is possible 
    to display all of the square numbers below one-hundred: 01, 04, 09, 16, 
    25, 36, 49, 64, and 81. 

    For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 
    9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube. 

    However, for this problem we shall allow the 6 or 9 to be turned 
    upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 
    4, 6, 7} allows for all nine square numbers to be displayed; otherwise 
    it would be impossible to obtain 09. 

    In determining a distinct arrangement we are interested in the digits on 
    each cube, not the order. 

    {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5} {1, 2, 3, 4, 5, 
    6} is distinct from {1, 2, 3, 4, 5, 9} 

    But because we are allowing 6 and 9 to be reversed, the two distinct 
    sets in the last example both represent the extended set {1, 2, 3, 4, 5, 
    6, 9} for the purpose of forming 2-digit numbers. 

    How many distinct arrangements of the two cubes allow for all of the 
    square numbers to be displayed? """ 


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

