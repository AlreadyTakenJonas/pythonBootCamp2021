#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:59:03 2021

@author: jonas
"""

from pathlib import Path
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#
#   READ / PARSE DATA
#
raw_data = Path("data.txt").read_text().splitlines()
raw_data = [ row.split("\t") for row in raw_data ]
data = {"x": [], "y": []}
for row in raw_data:
    row = [ float(number) for number in row ]
    data["x"].append(row[0])
    data["y"].append(row[1])
# Convert to numpy
data = { "x": np.array(data["x"]),
         "y": np.array(data["y"])}
    

# Create model with gauss curve
model = lambda x, A, b, c : A* np.exp(-(x-c)**2 * b )
# Fit Training data
fit = curve_fit(f = model,
                xdata = data["x"],
                ydata = data["y"],
                p0 = [700, 1, 600])
# Extract fitted parameters
param = fit[0]

# Predict training data with model
newData = {"x": data["x"], 
           "y": [model(x, param[0], param[1], param[2]) for x in data["x"]]}

# Plot data and regression
plt.plot("x", "y", data=data, label = "training data")
plt.plot("x", "y", data = newData, label = "Model")