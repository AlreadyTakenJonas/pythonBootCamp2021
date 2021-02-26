#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:01:02 2021

@author: jonas
"""

"""

This is a very inconvenient calculator. It does addition, subtraction, division and multplication of two numbers.

"""

# Print explanation for user
print("Best Calculator EVER!\nNote: You may compute only one operations with two operands.")

# Get the expression the user wants to compute
user_input = input("Enter your equation.\n > ")

# Split the user input into operands and operator
operation = user_input.split()

# Check if the user input is as expected. Should be two operands and one operator.
if len(operation) != 3:
    # Exit. Wrong user input.
    print("I can't read that. Please enter only one operation and put spaces between the operator and the operands.")

else:
    # Process user input
    
    # Convert operands into floats
    first_operand = float(operation[0])
    second_operand = float(operation[2])

    # Interpret user input and do the computation
    if operation[1] == "+":
        # Addition
        result = first_operand + second_operand
    elif operation[1] == "-":
        # Subtraction
        result = first_operand - second_operand
    elif operation[1] == "/":
        # Division
        result = first_operand / second_operand
    elif operation[1] == "*":
        # Multiplication
        result = first_operand * second_operand
    else:
        result = "?"
        print(f"Unknown operator {operation[1]}! Known operators: +, -, /, *.")    

    # Output result
    print(f"{user_input} = {result}")
    