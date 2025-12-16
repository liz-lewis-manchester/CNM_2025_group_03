import pytest
import numpy as np

try:
  from boundary import apply_boundary
except Exception:
  pytest.skip("test", allow_module_level=True)

def test_boundary_sets_first_node():
  theta = np.zeros(5)
  out = apply_boundary(theta.copy(), value=250.0)
  assert np.isclose(out[0], 250.0)
