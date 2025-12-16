import numpy as np
import pytest

# conftest.py makes /src importable
from grid import make_grid

def test_grid_endpoints_and_spacing():
  L, dx = 20.0, 0.2
