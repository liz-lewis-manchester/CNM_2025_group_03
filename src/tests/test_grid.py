import numpy as np
import pytest

# conftest.py makes /src importable
from grid import make_grid

def test_grid_endpoints_and_spacing():
  L, dx = 20.0, 0.2
  T, dt = 300.0, 10.0

x, t = make_grid(L, dx, T, dt)

# Endpoints
assert np.isclose(x[0], 0.0)
assert np.isclose(x[-1], L)
assert np.isclose(t[0]. 0.0)
assert np.isclose(t[-1], T)

# Uniform spacing
assert np.allclose(np.diff(x), dx)
assert np.allclose(np.diff(t), dt)

def test_grid_length_match_expected_counts():
  L, dx = 20.0, 0.2
  T, dt = 300.0, 10.0

  x, t = make_grid(L, dx, T, dt)

  expected_nx = int(round(L / dx)) + 1
  expected_nt = int(round(T / dt)) + 1

assert len(x) == expected_nx
assert len(t) == expected_nt

def test_grid_rejects_non_positive_inputs():
  with pytest.raises(ValueError):
    make_grid(0.0, 0.2, 300.0, 10.0)

  with pytest.raises(ValueError):
    make_grid(20.0, -0.2, 300.0, 10.0)
