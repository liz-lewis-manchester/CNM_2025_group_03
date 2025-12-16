from __future__ import annotations

def inflow_concentration(t: float, C0: float, mode: str = "pulse") -> float:
  if mode not in {"pulse", "constant"}:
    raise ValueError("mode must be 'pulse' or 'constant'")
  if mode == "constant":
    return C0

  # pulse: only at t=0
  return C0 if t == 0.0 else 0.0
