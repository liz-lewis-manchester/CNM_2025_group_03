import pandas as pd

# encoding latin1 to avoid error when reading mu
input = pd.read_csv("initial_conditions.csv",encoding="latin1");

Distance=input["Distance (m)"]
Concentration=input["Concentration (µg/m_ )"]

# quick test that the file contents are read correctly
assert Distance[5] == 5
assert Concentration[5] == 8

riverLength = Distance[20] # e.g. 20 m
spatialResolution = 0.2 # 20 cm

# assume that the initial resolution is the same for the whole file
# everything in metres
initialResolution = Distance[1] - Distance[0]
numberOfInterpolations = initialResolution / spatialResolution

# e.g. inital length 21 becomes 101 when adding 4 interpolation points
interpLength = (len(Concentration) - 1) * numberOfInterpolations + 1
print(interpLength)
print(numberOfInterpolations)
