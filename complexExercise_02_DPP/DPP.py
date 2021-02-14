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
# Plot all polarograms
for graph in polarograms:
    plt.plot("voltage", "current", data = graph, label = str(graph["concentration"]) + " mg/L")
# Add a legend
plt.legend(title = "Ion Concentration", prop={'size': 8})
# Add title
plt.title("Polarograms of Pb-, Zn- and Cd-Ions")
# Add axis labels
plt.ylabel("current Q / A")
plt.xlabel("voltage U / V")
# Save plot as image
plt.savefig( str(workingDir) + "/img/polarograms.png" )


#
#   STEP 3 : EXTRACT PEAK HEIGHT CHANGES
#

# Define peak locations (known from literature)
peakLocations = {"Pb": -0.340, "Cd": -0.555, "Zn": -0.959}

peakHeightChange = []
for ion, peakLocation in peakLocations.items():
    currentChange = [ graph["current"][graph["voltage"].index(peakLocation)] for graph in polarograms ]
    #
    # TODO : peakLocations are not part of the voltage axis. Interpolate voltages!!!!!!!
    #
    
    

# Handle arrays and math
# import numpy as np