#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:31:21 2021

@author: jonas
"""

"""

    This programm plays the game FizzBuzz. It counts through the integers between 0 and 100. 
    If the number is divisible by 3 it prints "Fizz". If divisible by 5 "Buzz" and if both "FizzBuzz".

"""

#   DEFINE SOME CONSTANTS
#
# The program will count from zero to INTERVAL (including INTERVAL)
INTERVAL = 100

# Define the rules of the game:
# Every number will be checked, if it is divisable by the values of the dictionary RULES
# If a number is a multiple of the value, the key of this value will be printed to the screen.
RULES = { "Fizz":  3,
          "Buzz":  5,
          "Bizz": 11,
          "Fuzz":  4  }

#   PLAY FIZZBUZZ
#
# Loop over all numbers between zero and INTERVAL
for number in range(INTERVAL+1):
    # Create an empty string that will be filled and printed to the screen
    output = ""
    
    # Loop over all rules in the dictionary RULES
    for phrase, divisor in RULES.items():
        # Check if the current number matches any of the rules
        if number % divisor == 0:
            # If the current number matches a rule: Add the corresponding phrase to the output string
            output += phrase
            
    # Print the result to the screen
    if output == "":
        # Print the current number if it matches no rule
        print(number)
    else:
        # Print the text instead of the current number
        print(output)