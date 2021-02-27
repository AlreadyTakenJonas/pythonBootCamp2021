#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:30:12 2021

@author: jonas
"""


"""
    
    This program reads the alphabet and the numbers 
    from 0 to 9 from a bunch of files and combines prints the information to the screen.

"""

#   IMPORT MODULES
#
# Handling files and paths
from pathlib import Path

#   CODE
#
# Get the working directory 
workingDir = Path(__file__).parent.absolute()
# Get generator with all files containing the alphabet and numbers
unsorted_file_list_alphabet = (workingDir/"data").glob("alphabet*")
unsorted_file_list_numbers = (workingDir/"data").glob("number*")
# Sort the files by name, makes sure that the data is ordered correctly
file_list_alphabet = sorted(unsorted_file_list_alphabet)
file_list_number = sorted(unsorted_file_list_numbers)

# Print the content of the files
output = ""
# Add the alphabet to an empty string
for file in file_list_alphabet:
    output += file.read_text().replace("\n", " ")
# Add the number list to the string with the alphabet
output += "\n"
for file in file_list_number:
    output += file.read_text().replace("\n", " ")
# Print the string with the alphabet and the numbers to the console
print(output)