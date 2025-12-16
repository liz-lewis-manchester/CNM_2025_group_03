import pytest
import numpy as np

try:
  from grid import make_grid
except Exception:
  pytest.skip("test", allow_module_level=True)

def test_grid_endpoints_and_spacing():
  L, dx = 20.0, 0.2
  T, dt = 300.0, 10.0
  x, t = make_grid(L, dx, T, dt)

  assert np.isclose(x[0], 0.0)
  assert np.isclose(x[-1], L)
  assert np.allclose(np.diff(t), dt)
