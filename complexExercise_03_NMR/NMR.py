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