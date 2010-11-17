import sys
import os
import math

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

       

        


