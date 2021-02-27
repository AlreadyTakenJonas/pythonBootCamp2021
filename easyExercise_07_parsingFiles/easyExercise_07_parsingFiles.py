#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:56:20 2021

@author: jonas
"""

"""

    This program reads a file and converts the content of the file into an array    

"""

#   IMPORT MODULES
# Handling files and paths
from pathlib import Path
# Create nice looking tables
from tabulate import tabulate


#   CODE

# Read the file
content = Path("measuredData.txt").read_text()

#   Parsing the file
# Split the file in rows and ignore the header
content = content.splitlines()[21:]
# Loop over all rows of the file and split them in two columns
# Convert the strings into numbers
data = [    [ float(row.split("\t")[0]) for row in content ],
            [ float(row.split("\t")[1]) for row in content ]    ]

# Format the data into a pretty table
data_table = tabulate(
    # Extract the ion and fitting parameters and put them into a list
    zip(data[0], data[1]),
    # Add descriptive headers for the table
    headers = ["Column 1", "Column 2"] 
)
# Print the table
print(data_table)