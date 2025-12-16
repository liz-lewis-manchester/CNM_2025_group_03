# Tests for grid creation
import pytest
import numpy as np

# imports function
try:
  from grid import make_grid
except Exception:
  pytest.skip("test", allow_module_level=True)

# checks grid endpoints and uniform spacing in spcae and time
def test_grid_endpoints_and_spacing():
  # Example parameters from test case 1
  L, dx = 20.0, 0.2
  T, dt = 300.0, 10.0
  x, t = make_grid(L, dx, T, dt)

  assert np.isclose(x[0], 0.0)
  assert np.isclose(x[-1], L)
  assert np.allclose(np.diff(x), dx)


  assert np.isclose(x[0], 0.0)
  assert np.isclose(x[-1], t)
  assert np.allclose(np.diff(t), dt)
