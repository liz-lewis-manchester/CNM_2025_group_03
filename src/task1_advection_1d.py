import numpy as np
import matplotlib.pyplot as plt

L = 20.0
dx = 0.2
T = 300.0
dt = 10.0
U = 0.1

x = np.arange(0.0, L + dx, dx)
t = np.arange(0.0, T + dt, dt)
Nx, Nt = len(x), len(t)

C = np.zeros((Nt, Nx))

# initial condition: 250 at x=0, 0 elsewhere
C[0, 0] = 250.0

a = (1.0/dt) + (U/dx)
b = (U/dx)

for n in range(1, Nt):
    # first 10s only
    C[n, 0] = 250.0 if n == 1 else 0.0

    for i in range(1, Nx):
        C[n, i] = ((1/dt)*C[n-1, i] + (U/dx)*C[n, i-1]) / ((1/dt) + (U/dx))


# plotting
for minutes in [0, 1, 2, 3, 4, 5]:
    n = int((minutes * 60) / dt)
    plt.plot(x, C[n, :], label=f"{minutes} min")

plt.xlabel("x (m)")
plt.ylabel("C (µg/m³)")
plt.legend()
plt.show()


