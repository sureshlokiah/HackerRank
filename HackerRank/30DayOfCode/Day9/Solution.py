#!/usr/bin/python3

##  
## Hacker Rank 30 Days of Code 
## Day 8: Dictionaries and Maps
## Suresh Lokiah
## 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    N = int(str(input()).strip())
    s = factorial(N)
    print(s)

