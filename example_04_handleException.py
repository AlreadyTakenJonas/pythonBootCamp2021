#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:30:27 2021

@author: jonas
"""

# Handling files and paths
from pathlib import Path

#
#   READ FILE WITH TRY-CATCH
#
# Ask user for a file to read. Ask again if file does not exist
while True:
    try:
        # Ask for file path
        user_filename = input("Enter file name: ")
        
        # Try to read file without checking if it exists
        file = Path(user_filename)
        print(f"Reading {str(file)} ...")
        content = file.read_text()
        
        # Leave the while loop
        break
    
    except FileNotFoundError:
        # Catch Exception: File was not found. Ask user again.
        print("File not found! Try again.")
    
# Continue with the rest of the program
print(content)

#
#   READ FILE WITHOUT TRY-CATCH
#
# Ask user for a file to read.
user_file = input("Enter file name: ")
user_file = Path(user_file)
# Ask the user again, if the file does not exist
while user_file.is_file() == False:
    user_file = input("File not found. Enter new file name: ")
    user_file = Path(user_file)
    
# Read text
content = user_file.read_text()
# Continue with the rest of the program    
print(content)
