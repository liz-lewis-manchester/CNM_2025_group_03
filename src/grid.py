from __future__ import annotations

import numpy as np

def make_grid(L: float, dx: float, T: float, dt: float) -> tuple[np.ndarray, np.darray]:

if L <= 0 or dx <= 0 or T <= 0 or dt <= 0:
  raise ValueError("L, dx, T, dt must all be positive")
  
# Rounding L/dx to an integer
Nx = int(round(L / dx))
Nt = int(round(T / dt))

x = np.linspace(0.0, L, Nx + 1)
t = np.linspace(0.0, T, Nt + 1)

return x, t
