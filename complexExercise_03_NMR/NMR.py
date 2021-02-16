#
#   This script uses the data from spin echo experiments to determine
#   the half life etime of the magnetisation of the samples spins
#

#
#   STEP 1 : READ DATA FROM FILES
#

#   IMPORT MODULES
# Handling files and paths
from pathlib import Path
from matplotlib import pyplot as plt

#   CODE
#
# Get the working directory 
workingDir = Path(__file__).parent.absolute()
# Get generator with all data files
dataFiles = (workingDir/"data").glob("*.txt")
# Sort the files by name, makes sure that the data is ordered by concentration
dataFiles = sorted(dataFiles)

# Process each file and add data to empty data structure
spinechos = []
# Process files
for file in dataFiles:
    print("Read file:", file)
    # Read file 
    content = file.read_text().splitlines()
    # Save the first line of the file as description of the data
    # Replace German number notation (1,2) by English number notation (1.2)
    # Remove tailing spaces with .strip()
    sample = content[0].strip().replace(",", ".")
    # Extract the data from the file
    # Replace German number notation (1,2) by English number notation (1.2)
    data    = [ line.replace(",", ".").split() for line in content[3:] ]
    # Reorganise the data and convert strings to floats
    time    = [ float(dataPair[0]) for dataPair in data ]
    voltage = [ float(dataPair[1]) for dataPair in data ]
    spinechos.append({"sample" : sample,
                      "time"   : time,
                      "voltage": voltage })
    
#   PLOT PROGRESS
for graph in spinechos:
    # Add the data as scatter plot
    plt.scatter("time", "voltage", data = graph, label = graph["sample"])
    # Add the data a second time as line graph to make the plot easier to read
    # label = None is important, because I use plt.scatter AND plt.plot for the same plot
    # label = None ensures that the legend works properly and each label is added only once
    plt.plot("time", "voltage", data = graph, label = None)
# Add legend
plt.legend(fontsize=8)
# Add title and labels
plt.title("Loss of Magnetisation")
plt.xlabel("time t / ms")
plt.ylabel("voltage ΔU / V")
# Show the plot  and allow creation of a new plot
plt.show()

#
#   STEP 2 : EXPONENTIAL FIT, HALF-LIFE TIME AND PLOT THE PROGRESS
#

#   IMPORT MODULE
# Used for fitting arbitrary functions
from scipy.optimize import curve_fit
# Math and stuff
import numpy as np

# Define the general form of an exponential decay
expFct = lambda time, A, b : A*np.exp(-b*time)
# Create empty data structure for fitting parameters
fitParam = []
# Loop over all measurements and fit the data with exponential function
for graph in spinechos:
    # Fit the data
    fit = curve_fit(f     = expFct, 
                    xdata = graph["time"], 
                    ydata = graph["voltage"],
                    # Initial guess of the fitting parameters
                    p0    = [10, 0.001])
    
    # Extract fitted parameters
    # Compute half life time of magnetisation as -ln(0.5)/b (derived from definition 
    # of exponential decay: voltage=A*exp(-b*time) )
    fitParam.append({"sample"        : graph["sample"],
                     "A"             : fit[0][0],
                     "b"             : fit[0][1],
                     "half-life-time": -np.log(0.5)/fit[0][1] })
    
    # Create a plot with the regression
    # Add raw data to the plot
    plt.scatter("time", "voltage", data = graph, label = graph["sample"])
    # Compute regression curve within the interval of the raw data
    # Get a time axis ranging from the smalles and biggest time value with a stepsize of 0.1
    fit_time    = np.arange(min(graph["time"]), max(graph["time"]), 0.1)
    # Evaluate the exponential decay function with the fitted parameters
    fit_voltage = expFct(time = fit_time, A = fit[0][0], b = fit[0][1]) 
    # Plot the calculated curve as line plot
    # label = None is important, because I use plt.scatter AND plt.plot for the same plot
    # label = None ensures that the legend works properly and each label is added only once
    plt.plot( fit_time, fit_voltage, label = None )

# Add legend to the plot
plt.legend(fontsize=8)
# Add labels and title
plt.title("Exponential Regression of Spin Echos")
plt.xlabel("time t / ms")
plt.ylabel("voltage ΔU / V")
# Save as image file
# IMPORTANT: use this command before plt.show!
plt.savefig(str(workingDir)+"/img/regression.png")
# Show the plot (optional)
plt.show()

#
#   STEP3 : CREATE A TABLE AND WRITE IT TO FILE
#

#   IMPORT MODULES
# Convert arrays into tables
from tabulate import tabulate

#   CODE
# Format the data into a pretty table
resultsTable = tabulate(
    # Extract the ion and fitting parameters and put them into a list
    [ sample.values() for sample in fitParam ],
    # Add descriptive headers for the table
    headers = ["Sample", "A / V", "b / (1/ms)", "half-life time t / ms"] 
)
# Print table to console
print("Exponential Regression:\n ΔU = A * exp(-b * time)")
print(resultsTable)
# Write table to file
print("Write results to file.")
(workingDir/"img/results.txt").write_text("Exponential Regression:\n ΔU = A * exp(-b * time)\n"+resultsTable+"\n")