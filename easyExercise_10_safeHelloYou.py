#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:23:59 2021

@author: jonas
"""

# Get user input
name = input("Enter your name: ")
age_string = input("Enter your age: ")

try:
    # Convert the user input into an integer
    age = int(age_string)
    
except ValueError:
    # Exit the program, because the user didn't enter the age as integer
    print("Your age must be an integer! Exiting the program.")
    raise SystemExit
    
# Greet the user.
print(f"Hello, {name}. I heard your {age} years old.")