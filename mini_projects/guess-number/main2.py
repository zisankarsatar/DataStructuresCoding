#! /usr/bin/env python3

import math
import os
import random
import re
import sys

# if __name__ == '__main__':
#     n = int(input().strip())
    
n = int(input('pls type nmbr: ').strip())    

condition1 = [2,4]

print(n**2)
if (n % 2) == 0:
    if n in condition1:
        print('Not Weird')
    elif (n > 6) & (20 > n):
        print('Weird')
    else  :
        print('Not Weird')
    
else : 
    print('Weird')
    