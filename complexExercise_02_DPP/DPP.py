#
#   This script uses differential pulse polarography to construct calibration curves from
#   measured polarogramms
#

#
#   STEP 1 : READ FILES
#

#   IMPORT MODULES
# Handling files and paths
from pathlib import Path
# Use Regular expression (extracting information from strings)
import re

#   CODE
#
# Get the working directory 
workingDir = Path(__file__).parent.absolute()
# Get generator with all data files
dataFiles = (workingDir/"data").glob("*.txt")
# Sort the files by name, makes sure that the data is ordered by concentration
dataFiles = sorted(dataFiles)

# Process each file and add data to empty data structure
polarograms = []
# Process files
for file in dataFiles:
    print("Read file:", file)
    # Extract concentration from the file name
    concentration = float(re.findall("\d+", file.name)[0])
    # Read the file and store an array of text lines
    content = file.read_text().splitlines()
    # Extract the lines containing the data by including only lines starting with a "-"
    # line[0] instead of line[:1] will cause an error if line is an empty string
    # Split every line into two columns with .split("\t")
    content = [ line.split("\t") for line in content if line[:1] == "-" ]
    # Save the first column as a float array
    voltage = [ float(line[0]) for line in content ]
    # Save the second column as float array
    current = [ float(line[1]) for line in content ]
    # Add data to data structure
    polarograms.append({"concentration" : concentration,
                        "voltage"       : voltage,
                        "current"       : current})


#
#   STEP 2 : PLOT THE RAW DATA
#

#   IMPORT MODULES
# Plotting module
from matplotlib import pyplot as plt

#   CODE
# Plot all polarograms
# Create new empty plot
# Here I used the return values of plt.subplots fig and ax to make the plot
# Usually I use plt.plot and so on, but in this case I needed the functions invert_xaxis and invert_yaxis.
# These functions are only accessible this way.
fig, ax = plt.subplots()
# Add the polarograms to the plot
for graph in polarograms:
    ax.plot("voltage", "current", data = graph, label = str(graph["concentration"]) + " mg/L")
# Add a legend
ax.legend(title = "Ion Concentration", prop={'size': 8})
# Invert x- and y-axis, because that's the way polarograms are usually drawn
ax.invert_xaxis()
ax.invert_yaxis()
# Add title
ax.set_title("Polarograms of Pb-, Zn- and Cd-Ions")
# Add axis labels
ax.set_ylabel("current I / A")
ax.set_xlabel("voltage U / V")
# Show plot
plt.show()
# Save plot as image
fig.savefig( str(workingDir) + "/img/polarograms.png" )


#
#   STEP 3 : EXTRACT PEAK HEIGHT CHANGES
#

#   IMPORT MODULE
# Handle arrays, interpolation and math
import numpy as np

# Define peak locations (known from literature)
peakLocations = {"Pb": -0.340, "Cd": -0.555, "Zn": -0.959}

# Extract peak height for every ion from every polarogram and combine information in one data structure
# Create empty data structure
peakHeightChange = []
# Loop over all ions
for ion, peakLocation in peakLocations.items():
    # Loop over all polarograms
    # Interpolate the polarograms, because the voltages given by the literature aren't part of the data set
    # np.interp interpolates the x-y-pairs (voltage-current) of the data at the given voltage value
    # np.interp need x values in increasing order -> [::-1] reverses the order of the array
    currentChange       = [ np.interp(peakLocation, graph["voltage"][::-1], graph["current"][::-1]) for graph in polarograms ]
    # Get the ion concentrations
    concentrationChange = [ graph["concentration"]                                      for graph in polarograms ]
    # Add data to the data structure
    # Save current and concentration as np.array with .reshape(-1,1),
    # because the linear regression needs them in this format
    peakHeightChange.append({"ion"          : ion,
                             "concentration": np.array(concentrationChange).reshape(-1,1),
                             "current"      : np.array(currentChange)                        })
    
#   PLOT THE PROGRESS
# Enter the data organised by ion as scatter plot
for graph in peakHeightChange:
    plt.scatter("concentration", "current", data=graph, label=graph["ion"]+"^2+")
# Adjust the a-axis limit by computing the maximum and minimum of all y-values
# List comprehension combines the values from differnent arrays in one combined array
# I have no idea why pyplot needs me to do this shit.
plt.ylim( max([current for current in graph["current"] for graph in peakHeightChange])*0.5,
          min([current for current in graph["current"] for graph in peakHeightChange])*1.1  )
# Add legend
plt.legend()
# Add title and labels
plt.title("Calibration of the Polarograph")
plt.xlabel("concentration c / (mg/L)")
plt.ylabel("current I / A")
# Show plot and allow creation of a new plot
plt.show()

#
#   STEP 4 : LINEAR REGRESSION
#

#   IMPORT MODULE
# Module for machine learning -> linear regression
from sklearn.linear_model import LinearRegression
# Convert arrays into tables
from tabulate import tabulate

# Do linear regression
# Create a linear model and pass the peakHeightChange to the model
linearFits = []
# Loop over all ions
for graph in peakHeightChange:
    # Do the linear regression
    fit = LinearRegression().fit( graph["concentration"], 
                                  graph["current"] )
    # Add linear fit to the empty data structure
    linearFits.append( {"ion": graph["ion"],
                        "fit": fit           })

#   PLOT
# Enter the data organised by ion as scatter plot and the corresponding linear fit
# zip enables us to loop over to lists at the same time,
# getting for the first iteration the first elements of both lists, for the second iteration the second elements, ...
for graph, fit in zip(peakHeightChange, linearFits):
    # Add the peak height as scatter plot
    plt.scatter("concentration", "current", data=graph, label=graph["ion"]+"^2+")
    # Add the linear regression as line plot
    # label = None is important, because I use plt.scatter AND plt.plot for the same plot
    # label = None ensures that the legend works properly and each label is added only once
    plt.plot(graph["concentration"], fit["fit"].predict(graph["concentration"]), label=None)
# Adjust the a-axis limit by computing the maximum and minimum of all y-values
# List comprehension combines the values from differnent arrays in one combined array
# I have no idea why pyplot needs me to do this shit.
plt.ylim( max([current for current in graph["current"] for graph in peakHeightChange])*0.5,
          min([current for current in graph["current"] for graph in peakHeightChange])*1.1  )
# Add legend
plt.legend()
# Add title and labels
plt.title("Calibration of the Polarograph")
plt.xlabel("concentration c / (mg/L)")
plt.ylabel("current I / A")
# Save as image file
# IMPORTANT: use this command before plt.show!
plt.savefig(str(workingDir)+"/img/regression.png")
# Show plot (optional)
plt.show()

#   PRINT PRETTY TABLE
# Extract the fitting parameters from linearFits and make a pretty table
fittingCoeffienceTable = tabulate(
    # Extract the ion and fitting parameters and put them into a list
    [ [fit["ion"]+"^2+", fit["fit"].coef_[0], fit["fit"].intercept_] for fit in linearFits ],
    # Add descriptive headers for the table
    headers = ["Ion", "slope / (A*L/mg)", "intercept / A"] 
)
# Print the pretty table
print(fittingCoeffienceTable)
print("I = slope * c + intercept")


#
#   USE THE CALIBRATION FOR SOMETHING INTERESTING
#   SIMILAR TO PREVIOUS EXAMPLE ABOUT FLUORESCENCE
#