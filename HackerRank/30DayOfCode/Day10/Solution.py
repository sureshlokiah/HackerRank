#!/usr/bin/python3

##  
## Hacker Rank 30 Days of Code 
## Day 10: Binary Numbers
## Suresh Lokiah
## 

import math
import os
import random
import re
import sys


if __name__ == "__main__":
    n = int(input())
    print(max(len(seq1) for seq1 in bin(n)[2:].split('0')))

