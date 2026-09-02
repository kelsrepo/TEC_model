import numpy as np
import pandas as pd
from src.energy_balance import solve_operating_point

def run_sweep(Qc_interp, Ptec_interp, I_range, dT_range, T_in_range, pr_range):
    results = []
    for I in I_range:
        for dT in dT_range:
            for T_in in T_in_range:
                for pr in pr_range:
                    try:
                        r = solve_operating_point(I, dT, T_in, pr, Qc_interp, Ptec_interp)
                        results.append(r)
                    except ValueError:
                        continue
    return pd.DataFrame(results)