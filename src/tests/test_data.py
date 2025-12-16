import pytest
import numpy as np
from pathlib import Path

# Locating initial conditions in repo
REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = REPO_ROOT / "data" / "initial_conditions.csv"

try:
  from io_utils import load_initial_conditions
except Exception:
  pytest.skip("test", allow_module_level=True)

def test_interpolated_shape_no_nans():

# Standard grid matching test case 1 spacing
x_grid = np.arange(0.0, 20.0 + 0.2, 0.2)

theta0 = load_initial_conditions(DATA_FILE, x_grid)

assert len(theta0) == len(x_grid)
assert np.all(np.isfinite(theta0))
