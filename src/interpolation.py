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
