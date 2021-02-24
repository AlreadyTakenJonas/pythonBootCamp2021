#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:27:36 2021

@author: jonas
"""

"""

This program will ask your name and age to greet you.

"""

# Get the users name
user_name = input("Hi, there! What's your name?\n > ")

# Greet by adding name and greeting
print("Hello, " + user_name + "!")
# Greet by joining an array of strings
print("".join(["Hello, ", user_name, "!"]))
# Greet by using a formatting string ('f' in front of the string)
print(f"Hello, {user_name}!")

# Get users age
user_age = input(f"How old are you, {user_name}?\n > ")
# Convert user age to integer
user_age = int(user_age)

# Mock the user by omitting the first and last letter of his name and spelling it backwards
print(f"{user_name[-2:0:-1]} ({user_age}) doesn't like Tom Hanks.")