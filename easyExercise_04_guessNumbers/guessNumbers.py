#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:13:12 2021

@author: jonas
"""

"""

This program makes you guess a random integer.

"""

# Import function generating random integers
from random import randint

# Get a random integer between 0 and 5.
number = randint(0, 5)

# Let the user guess numbers until he/she is right
numberGuessed = False
while numberGuessed == False:
    # Ask for user input and convert the input to an integer
    guess = int( input("Guess a number between 0 and 5.") )
    # Compare the guess with the random number
    numberGuessed = (number == guess)
    # Tell the user he is wrong, if he is wrong
    if !numberGuessed:
        print("Wrong guess! Try again.")
        
# Tell the user he is correct and exit
print("Correct!")