import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# encoding latin1 to avoid error when reading mu
initial_conditions = pd.read_csv("initial_conditions.csv",encoding="latin1");

Distance=initial_conditions["Distance (m)"]
Concentration=initial_conditions["Concentration (µg/m_ )"]

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
interpLength = int((len(Concentration) - 1) * numberOfInterpolations + 1)
print(interpLength)
print(numberOfInterpolations)

# interpolating first column
# again assuming evenly spaced
newD = np.linspace(Distance[0], Distance[20], num=interpLength)

# interpolating second column using newD
newC = np.interp(newD, Distance, Concentration)
# print(newC)

# scatter plot to test if interpolation looks correct
plt.scatter(Distance, Concentration, label='original')

plt.scatter(newD, newC, label='interpolated', s=1)

plt.legend()

plt.show()



totalT=float(input("Input total time period here (in seconds): "))

temporalRes=float(input("Input temporal resolution here (in seconds): "))

u=float(input("Input river velocity (in m/s): "))

dx = spatialResolution

CFLmax = 1
dt = CFLmax * dx / u

plotInterval = math.ceil(int(temporalRes / dt)) # rounds up to prevent plot interval being 0

Nt = int(totalT / dt)

Nx = interpLength

x=newD

y = newC.copy()

plt.figure()

for j in range( 1, Nt + 1 ):
    yOld = y.copy()
    for i in range(1, Nx - 1):
        y[i] = yOld[i] - u * dt * ( yOld[i] - yOld[i-1] ) / dx
    
    # boundary conditions
    y[0] = yOld[0] # continuous inflow of pollutant
    y[-1] = y[-2] # downstream boundary: 0 spatial gradient to allow outflow
    
    if j % plotInterval == 0:
        plt.plot(x, y)

plt.xlabel("Distance")
plt.ylabel("Concentration")
plt.show()

