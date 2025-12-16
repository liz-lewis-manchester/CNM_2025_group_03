from __future__ import annotations
import numpy as np

from grid import make_grid
from boundary import inflow_concentration

def run_simulation(
  L: float,
  dx: float,
  T: float,
  dt: float,
  U: float,
  C0 float = 250.0,
  inflow_mode: str = "pulse",
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:

  if U < 0:
        raise ValueError("This setup assumes U >= 0 (flow downstream).")

  x, t = make_grid(L, dx, T, dt)
  Nx = len(x) - 1
  Nt = len(t) - 1

   alpha = (U * dt) / dx


  Theta = np.zeros((Nt + 1, Nx + 1), dtype=float)

  Theta[0, 0] = C0
  Theta[0, 1:] = 0.0

  for n in range(0, Nt):
      theta_old = Theta[n, :].copy()
      theta_new = np.zeros_like(theta_old)

      theta_new[0] = inflow_concentration(t[n + 1], C0=C0, mode=inflow_mode)
      for i in range(1, Nx + 1):      
          theta_new[i] = (theta_old[i] + alpha * theta_new[i - 1]) / (1.0 + alpha)

        Theta[n + 1, :] = theta_new

    return Theta, x, t
  
