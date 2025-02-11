#! /usr/bin/env python3

import random

small_number = int(input("Please put small number: "))
big_number = int(input("Please put big number: "))

if small_number > big_number :
    print("siktir git")
    
#print(small_number, big_number)

guess_number = random.randint(small_number, big_number)

print(guess_number)

counter = 1
guess_number_user = int(input(f"pls put your guess ({counter}.): "))



    
while guess_number != guess_number_user:
    if guess_number > guess_number_user:
        print (f"go up ({counter})")
    else :
        print(f'try down ({counter})')
    
    if counter == 7 :
        counter += 1    
        break
    counter += 1    
    guess_number_user = int(input(f"pls type your guess ({counter}.): "))
    

if counter == 8:
    print("You failed, the guess was : {}".format(guess_number))
else:
    print(f'You guess it correct on {counter} times !!!') 
        
    
    
