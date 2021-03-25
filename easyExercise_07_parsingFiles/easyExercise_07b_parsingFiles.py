#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:46:15 2021

@author: jonas
"""


"""

    This program reads a file and converts the content of the file into an array.   

"""


from pathlib import Path
import numpy as np   

#
#   READ THE FILE
#
data_file = Path("complicatedData.txt")
raw_data = data_file.read_text()

#
#   PARSE FILE
#

# Splitting the data into an array of lines
data = raw_data.splitlines()
# Removing the header of the file; Each line of the header starts with '#'
data = [ row for row in data if row[0] != "#" ]
# Split each row into columns
data = [ row.split("\t") for row in data ]
# Convert every element into a floating point number
converted_data = []
for row in data:
    row = [ float(number) for number in row ]
    converted_data.append(row)
    
# Convert data into a numpy array
converted_data = np.array(converted_data)

