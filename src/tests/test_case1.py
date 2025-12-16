import numpy as np
import pytest

try:
    from solver import run_simulation
except Exception:
    pytest.skip("solver.run_simulation not implemented yet", allow_module_level=True)


def test_case1_runs_and_has_expected_structure():
    L, dx = 20.0, 0.2
    T, dt = 300.0, 10.0
    U = 0.1
    C0 = 250.0

    Theta, x, t = run_simulation(L=L, dx=dx, T=T, dt=dt, U=U, C0=C0, inflow_mode="pulse")

    # Shape checks
    assert Theta.shape == (len(t), len(x))

    # Initial condition checks
    assert np.isclose(Theta[0, 0], C0)
    assert np.allclose(Theta[0, 1:], 0.0)

    # Finite values
    assert np.all(np.isfinite(Theta))

    # Non-negative (allow tiny numerical noise)
    assert Theta.min() >= -1e-12

    # Pollutant should appear downstream at some later time
    assert np.max(Theta[1:, 1:]) > 0.0
