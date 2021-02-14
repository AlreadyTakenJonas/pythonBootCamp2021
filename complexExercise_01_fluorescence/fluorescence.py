#
#   This script uses fluorescence spectra of different solution with known concentration to
#   calculate an unknown concentration from given fluorescence intensity
#   Calculations are done in nano moles per liter
#



#
#   STEP 1 : READ DATA FROM FILE
#

#   IMPORT MODULES
#
# Handling files and paths 
from pathlib import Path
# Use Regex
import re


#   CODE
#
# Get the working directory 
workingDir = Path(__file__).parent.absolute()
# Get generator with all data files
dataFiles = (workingDir/"data").glob("*.ASC")
# Sort the files by name, makes sure that the data is ordered by concentration
dataFiles = sorted(dataFiles)

#   READ DATA FROM FILE
#
# Create empty data structur
spectra = []
# Read all data files and add data to empty data structure
for file in dataFiles:
    print("Read file: ", file.name)
    # Extract the concentration of the solution from the file name
    concentration = int(re.findall("\d{3}", file.name)[0]) # Concentration in nano mol per liter
    # Read the file
    content = file.read_text().splitlines()
    # Parse the file
    # -> Save the data in two columns of value float
    wavelength = [ float( line.split(", ")[0]                   ) for line in content ]
    intensity  = [ float( line.split(", ")[1].replace(",", ".") ) for line in content ]
    # Add data to data structure
    spectra.append( {"concentration": concentration, 
                     "wavelength"   : wavelength, 
                     "intensity"    : intensity      } )


#
#   STEP 2 : PLOT RAW DATA
#

#   IMPORT MODULES
# Plotting
from matplotlib import pyplot as plt
# Use numpy arrays
import numpy as np

#   CODE
print("Plot spectra")
# Create plot with all spectra
for spectrum in spectra:
    plt.plot("wavelength", "intensity", data = spectrum, 
             # Add the concentration to the legend
             label = str(spectrum["concentration"])+" nM" )
# Add legend 
plt.legend()
# Add grid
plt.grid()
# Add title
plt.title("concentration dependency of fluorescence spectra")
# Add axis labels
plt.ylabel("intensity")
# Use raw binary string to enable LaTeX encoding -> greek letters
plt.xlabel(r"wavelength $\lambda$ / $nm$")
# Save plot to file
plt.savefig( str(workingDir) + "/img/spectra.png" )


#
#   STEP 3 : FIND MAXIMUM AND EXTRACT PEAK HEIGHT
#

# Find the global maximum
# Define small function to return the index of the largest value
indexMax = lambda array : array.index(max(array))
# Get the index of the maximum
peakIndex = indexMax(spectra[0]["intensity"])
# Get the wavelength of the maximum
peakLocation = spectra[0]["wavelength"][peakIndex]

# Extract the concentration and the height of the maximum from the spectra
# Create new table with the information
# Use numpy arrays, because fitting the data requires them later on
peakHeightChange = {
    # Extract the concentration of each solution
    "concentration": np.array(
        [ spectrum["concentration"]                                         for spectrum in spectra ]
    ),
    # Extract the intensity value from each spectra at the same wavelength
    # spectrum["wavelength"].index(peakLocation) returns the index of the interesting wavelength
    # spectrum["intensity"][ ... ] returns the intensity at the wavelength of the largest peak in the spectra
    "intensity"    : np.array(
        [ spectrum["intensity"][spectrum["wavelength"].index(peakLocation)] for spectrum in spectra ]
    )
}

# Plot the progress
# Create new empty plot
plt.subplots()
# Plot the peak height change as scatter plot
plt.scatter("concentration", "intensity", data = peakHeightChange)
# Add labels and title
plt.title("Peak Height Change")
plt.xlabel("concentration c/nM")
plt.ylabel("intensity")

#
#   STEP 4 : APPROXIMATE BLIND VALUE
#

# Blind value was not measured. Blind value would be the spectrum with concentration zero.
# Approximate blind value by computing the mean of the lowest intenisty spectrum beyond 650nm.

# Define small function to return the index of the smallest value of the array
indexMin = lambda array : array.index(min(array))
# Get the index of the spectrum with the lowest concentration
lowConcentrationIndex = indexMin([ spectrum["concentration"] for spectrum in spectra ])
# Get the index of 650nm in the wavelength array
index650nm = spectra[lowConcentrationIndex]["wavelength"].index(650)
# Compute the mean of all intensities beyond 650 nm by slicing the array ( arr[index650nm:] )
blindValue = np.mean(spectra[lowConcentrationIndex]["intensity"][index650nm:])
# Add blind value to the table of peak height changes
peakHeightChange["concentration"] = np.append( peakHeightChange["concentration"], 0          )
peakHeightChange["intensity"]     = np.append( peakHeightChange["intensity"]    , blindValue )

# Plot the progress
# Create new empty plot
plt.subplots()
# Plot the peak height change as scatter plot
plt.scatter("concentration", "intensity", data = peakHeightChange)
# Add labels and title
plt.title("Peak Height Change")
plt.xlabel("concentration c/nM")
plt.ylabel("intensity")

#
#   STEP 5 : DO LINEAR REGRESSION
#

#   IMPORT MODULE
# Module for machine learning -> linear regression
from sklearn.linear_model import LinearRegression

# Do linear regression
# The x-values must be converted into a column-vector -> .reshape(-1,1)
peakHeightChange["concentration"] = peakHeightChange["concentration"].reshape(-1,1)
# Create a linear model and pass the peakHeightChange to the model
linearFit = LinearRegression().fit( peakHeightChange["concentration"], 
                                    peakHeightChange["intensity"] )

# Print formula of linear regression
print(linearFit.coef_[0], " * c + ", linearFit.intercept_)

# Define small function to predict concentration from measured peak height
predictConcentration = lambda intensity : (intensity - linearFit.intercept_)/linearFit.coef_[0]

# Create a lovely plot
# Create new empty plot
plt.subplots()
# Plot the peak height change as scatter plot
plt.scatter("concentration", "intensity", data = peakHeightChange, label="data")
# Draw regression line
plt.plot(peakHeightChange["concentration"], 
         linearFit.predict(peakHeightChange["concentration"]), 
         "r", label="fit")
# Add labels and title
plt.title("Peak Height Change")
plt.xlabel("concentration c/nM")
plt.ylabel("intensity I")
# Add grid to plot
plt.grid()
plt.legend()
plotDescription = "Regression: $I = a * c + b$ \n a = {}/nM \n b = {}".format(linearFit.coef_[0], linearFit.intercept_)
plt.text(200,0, plotDescription )
# Save plot to file
plt.savefig(str(workingDir)+"/img/regression.png")


#
#   STEP 6 : PREDICT CONCENTRATIONS
#    

# Ask for user input via console
print("Enter intensity I at", peakLocation, "nm for unknown sample concentration c.")
intensity = float(input("I = "))
# Predict with regression model
concentration = predictConcentration(intensity)
# Return result
print("The samples concentration is c =", str(concentration), "nmol/L")