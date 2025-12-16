# variable for the what number row the last row is, adjusting for first row being Distance=0
lastRow = len(Distance)-1

# gets river length from file
riverLength = (Distance[lastRow]) # e.g. len(Distance)=21, Distance[20]=20m

numberOfInterpolations = float(input("Input the number of interpolations required here. e.g. input 5 for a spatial resolution of 0.2: "))

# assume that the initial resolution is the same for the whole file
# everything in metres
initialResolution = Distance[1] - Distance[0]

# e.g. inital length 21 becomes 101 when adding 4 interpolation points
interpLength = int((len(Concentration) - 1) * numberOfInterpolations + 1)

# interpolating first column
# again assuming evenly spaced
newD = np.linspace(Distance[0], Distance[lastRow], num=interpLength)

# interpolating second column using newD
newC = np.interp(newD, Distance, Concentration)
# print(newC)

# scatter plot to test if interpolation looks correct
plt.scatter(Distance, Concentration, label='original')

plt.scatter(newD, newC, label='interpolated', s=1)

plt.legend()

plt.show()
