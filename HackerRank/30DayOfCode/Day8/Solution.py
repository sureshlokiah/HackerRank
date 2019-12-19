#!/usr/bin/python3

##  
## Hacker Rank 30 Days of Code 
## Day 8: Dictionaries and Maps
## Suresh Lokiah
## 

import sys

phonebook={}
name = phone = ""
n = int(str(input()))

for i in range(n):
    name,phone = str(input()).split()
    name  = name.strip()
    phone = phone.strip()
    
    ## datacheck
    if name.islower() and len(phone) == 8 and phone.isdigit():
        phonebook[name.strip()] = phone.strip()

while True:
    try:
        name = input()
        name = name.strip()    
        if name == "":
            break

        if (phonebook.get(name) != None):
            print("%s=%s" % (name,phonebook.get(name)))
        else:
            print('Not found') 
    except EOFError:
        break


