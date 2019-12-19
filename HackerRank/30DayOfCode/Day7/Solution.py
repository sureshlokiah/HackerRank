#!/usr/bin/python3

##  
## Hacker Rank 30 Days of Code 
## Day 7: 30-arrays-English
## Suresh Lokiah
## 

N = int(str(input()).strip())
strA = input().strip()
A = list(map(int, strA.split()[:N:][::-1]))
print(A)
