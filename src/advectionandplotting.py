totalT=float(input("Input total time period here (in seconds): "))

temporalRes=float(input("Input temporal resolution here (in seconds): "))

u=float(input("Input river velocity (in m/s): "))

dx = spatialResolution

CFLmax = 1
dt = CFLmax * dx / u

plotInterval = int(math.ceil(temporalRes / dt)) # rounds up to prevent plot interval being 0

Nt = int(totalT / dt)

# check Nt isn't 0
assert Nt != 0

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
    raise ValueError('The current end boundary condition causes the graph to go flat at the end.')
    
    if j % plotInterval == 0:
        plt.plot(x, y)

plt.xlabel("Distance")
plt.ylabel("Concentration")
plt.show()

plt.plot(x, newC, label="Initial")
plt.plot(x, y, label="Final")
plt.legend()
plt.show()
