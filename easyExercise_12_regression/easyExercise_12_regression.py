#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:20:35 2021

@author: jonas
"""

# IMPORT MODULES
# Handling linear regression
from sklearn.linear_model import LinearRegression
# Handling exponential regression
from scipy.optimize import curve_fit
# Handling numbers and arrays
import numpy as np
# Handling plots
from matplotlib import pyplot as plt

# Create some data to fit and plot
dummyData = { "x": np.array([ 0   , 1   , 2   ,  3   ,  4   ]),
              "y": np.array([ 1.11, 2.23, 7.39, 29.96, 49.40]) }

# Perform a linear regression on the data
linearFit = LinearRegression().fit( dummyData["x"].reshape(-1,1),
                                    dummyData["y"] )

# Perform an exponential regression on the data
# Define exponential function
expFct = lambda x, A, b : A*np.exp(b*x)
# Perform the fit
expFit = curve_fit(f = expFct,
                   # Training Data
                   xdata = dummyData["x"],
                   ydata = dummyData["y"],
                   # Initial values for fitting parameter
                   p0 = [1, 1])
# Compute the exponential curve to plot the fitting model
# Get sequence of x values in the interval of the training data
expCurve = {"x": np.arange( min(dummyData["x"]), max(dummyData["x"])+0.1, 0.1 )}
# Compute y values
expCurve["y"] = [ expFct(x, expFit[0][0], expFit[0][1]) for x in expCurve["x"] ]

#
#   PLOT DATA AND MODELS
#
# Plot data
plt.plot("x", "y", 
         "o", # Plot the data as scatter plot
         data=dummyData, 
         # Add label for legend and coloring
         label="data")
# Plot linear model
plt.plot(dummyData["x"], 
         # Predict training data with linear model
         linearFit.predict( dummyData["x"].reshape(-1,1) ),
         # Add label for legend and coloring
         label="linear model")
# Plot exponential model
plt.plot("x", "y",
         "", # Add empty format string. There is a warning if this parameter is not passed. 
         data=expCurve, 
         # Add label for legend and coloring
         label="exp model")
# Add legend to the plot
plt.legend()
# Add axis labels
plt.xlabel("x")
plt.ylabel("y")

# Save the plot as an image file
plt.savefig("regression.png")