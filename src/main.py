from __future__ import annotations
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from solver import run_simulation


RESULTS_DIR = Path(__file__).resolve().parents[1] / "results"
RESULTS_DIR.mkdir(exist_ok=True)


def plot_profiles(Theta: np.ndarray, x: np.ndarray, t: np.ndarray, times_to_plot: list[float], title: str, outpath: Path) -> None:
    plt.figure()
    for target_time in times_to_plot:
        # Find closest time index
        idx = int(np.argmin(np.abs(t - target_time)))
        plt.plot(x, Theta[idx, :], label=f"t={t[idx]:.0f}s")
    plt.xlabel("x (m)")
    plt.ylabel("Concentration (ug/m^3)")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath, dpi=200)
    plt.close()


def run_test_1():
    L, dx = 20.0, 0.2
    T, dt = 300.0, 10.0
    U = 0.1
    C0 = 250.0

    Theta, x, t = run_simulation(L=L, dx=dx, T=T, dt=dt, U=U, C0=C0, inflow_mode="pulse")

    plot_profiles(
        Theta, x, t,
        times_to_plot=[0, 60, 120, 180, 240, 300],
        title="Test 1: 1D advection (pulse at x=0)",
        outpath=RESULTS_DIR / "test1_profiles.png",
    )

    print(f"[OK] Test 1 complete. Saved: {RESULTS_DIR / 'test1_profiles.png'}")


def run_test_3_sensitivity():
    L, T = 20.0, 300.0
    C0 = 250.0

    # Baseline
    base = dict(L=L, dx=0.2, T=T, dt=10.0, U=0.1, C0=C0, inflow_mode="pulse")
    Theta0, x0, t0 = run_simulation(**base)

    # Sensitivity in U (same grid)
    for U in [0.05, 0.1, 0.2]:
        Theta, x, t = run_simulation(L=L, dx=0.2, T=T, dt=10.0, U=U, C0=C0, inflow_mode="pulse")
        plot_profiles(
            Theta, x, t,
            times_to_plot=[300],
            title=f"Sensitivity: U={U} m/s (profile at 300s)",
            outpath=RESULTS_DIR / f"sens_U_{U}.png",
        )

    # Sensitivity in dx (change grid)
    for dx in [0.1, 0.2, 0.4]:
        Theta, x, t = run_simulation(L=L, dx=dx, T=T, dt=10.0, U=0.1, C0=C0, inflow_mode="pulse")
        plot_profiles(
            Theta, x, t,
            times_to_plot=[300],
            title=f"Sensitivity: dx={dx} m (profile at 300s)",
            outpath=RESULTS_DIR / f"sens_dx_{dx}.png",
        )

    # Sensitivity in dt (change time grid)
    for dt in [5.0, 10.0, 20.0]:
        Theta, x, t = run_simulation(L=L, dx=0.2, T=T, dt=dt, U=0.1, C0=C0, inflow_mode="pulse")
        plot_profiles(
            Theta, x, t,
            times_to_plot=[300],
            title=f"Sensitivity: dt={dt} s (profile at 300s)",
            outpath=RESULTS_DIR / f"sens_dt_{dt}.png",
        )

    print(f"[OK] Test 3 plots saved in: {RESULTS_DIR}")


if __name__ == "__main__":
    run_test_1()
    run_test_3_sensitivity()

