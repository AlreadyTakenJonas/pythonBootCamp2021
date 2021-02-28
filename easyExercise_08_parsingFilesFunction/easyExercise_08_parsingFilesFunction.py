#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:27:10 2021

@author: jonas
"""

"""

    This programm uses a function to parse txt-files and convert them into a array

"""

#   IMPORT MODULES
# Handling files
from pathlib import Path
# Handling math and arrays
import numpy as np
# Create nice looking tables
from tabulate import tabulate

def parse_txt(path_to_file: (Path, str), length_header: int = 0) -> np.array:
    """
    This function reads a txt file and parses its content into a numpy array.

    Parameters
    ----------
    path_to_file : (Path, str)
        String or pathlib.Path object with the file to parse.
    length_header : int, optional
        The number of rows with meta information in front of the data. These rows will be removed before the text will be converted into a numpy.array. The default is 0.

    Returns
    -------
    data : numpy.array
        numpy.array containing numpy arrays with the data from the file.

    """
    # Convert path into an Path object, read the file, split the files content into an array of rows
    # Remove the first rows of the file containing uninteressting meta data
    content = Path(path_to_file).read_text().splitlines()[length_header:]
    
    # Loop over all rows of the file and split them in two columns
    # Convert the strings into numbers
    data = np.array([ [ float(row.split("\t")[0]) for row in content ],
                      [ float(row.split("\t")[1]) for row in content ] ])
    
    # Return the data frame
    return data


#   PARSE a bunch of files into numpy.arrays
# Get a sorted list of all files to process
files = sorted(Path("data").iterdir())
# Make a list with the length of each file header that must be removed.
header_lengths = [21] + [ 2 for i in range(0, len(files)-1) ]
# Parse the list of files into a dictionary of numpy arrays
measurements = { file.stem : parse_txt(file, header) for file, header in zip(files, header_lengths) }

# Print the parsed data to the console
for measurement, data in measurements.items():
    # Create a lovely table
    data_table = tabulate( 
        # Use only the first 5 rows and add dots as sixth line
        np.append(data.T[:5], [["...", "..."]], axis=0),
        # Add column headers
        headers = ["Column 1", "Column 2"],
        # format the tables pretty
        tablefmt="pretty" )
    # Print the result to the console
    print(f"\n     {measurement}:\n{data_table}")