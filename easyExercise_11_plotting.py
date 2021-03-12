#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:34:20 2021

@author: jonas
"""


"""

Exercise 11: Creating a plot with a legend

"""

# Create some dummy data
experimentOne = {"time": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                 "temperature": [100.00, 50.00, 33.33, 25.00, 20.00, 16.67, 14.29, 12.50, 11.11, 10.00] }
experimentTwo = {"time": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                 "temperature": [100.00, 36.79, 13.53,  4.98,  1.83,  0.67,  0.25,  0.09,  0.03,  0.01] }

# Import module that creates plots
from matplotlib import pyplot as plt

# Create a plot with the dummy data
# The parameter "-o" creates a lineplots with dot marks.
# The label parameter assures that the curves will be colored and added to the legend
# 
# Add first dictionary
plt.plot("time", "temperature", "-o", data = experimentOne, label = "MCFY")
# Add second dictionary
plt.plot("time", "temperature", "-o", data = experimentTwo, label = "BRWN")
# Add titles and axis labels
plt.title("Cooling Curve of Flux Capacitors")
plt.xlabel("Time $t$ / min")
plt.ylabel(r"Temperature $\vartheta$ / °C")
# Add a legend. Give the legend a descriptive title.
plt.legend(title = "Models")