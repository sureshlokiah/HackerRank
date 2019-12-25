#!/usr/bin/python3

##  
## Hacker Rank 30 Days of Code 
## Day 11: 2D Arrays
## Suresh Lokiah
## 

import math
import os
import random
import re
import sys

def printHourglasses(arr):
    # a+b+c+e+f+g+h
    maxSumHourglass = -10000000
    for r in range(len(arr) - 2):
        for c in range(len(arr[0]) - 2):
            curr_row_list = []
            middle_cell = []
            last_row_list = []
            sumHourglass=0
            # Current Row
            for i in range(3):
                c_i = c + i
                curr_row_list.extend([arr[r][c_i]])
                sumHourglass += int(arr[r][c_i])
                if i == 1:
                    middle_cell.extend([arr[r+1][c_i]])
                    sumHourglass += int(arr[r+1][c_i])
                last_row_list.extend([arr[r+2][c_i]])
                sumHourglass += int(arr[r+2][c_i])


            print("#####",r,c)
            print(curr_row_list)
            print(middle_cell)
            print(last_row_list)
            print(maxSumHourglass, sumHourglass)

            if maxSumHourglass < sumHourglass:
                maxSumHourglass = sumHourglass
    print(maxSumHourglass)



if __name__ == '__main__':
    arr = []

    for _ in range(2):
        arr.append(list(map(int, input().rstrip().split())))

    #arr.append("a b c d e f".split())
    #arr.append("g h i j k l".split())
    #arr.append("m n o p q r".split())

    #arr.append("00 01 02 03 04 05".split())
    #arr.append("10 11 12 13 14 15".split())
    #arr.append("20 21 22 23 24 25".split())

    #arr.append("1 1 1 0 0 0".split())
    #arr.append("0 1 0 0 0 0".split())
    #arr.append("1 1 1 0 0 0".split())
    #arr.append("0 0 2 4 4 0".split())
    #arr.append("0 0 0 2 0 0".split())
    #arr.append("0 0 1 2 4 0".split())
    #for i in range(len(arr)):
    #    print(arr[i])

    printHourglasses(arr)
    

    

