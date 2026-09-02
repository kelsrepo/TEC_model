from src.tec_interpolation import load_tec_model
from src.sweep import run_sweep
import numpy as np

Qc_interp, Ptec_interp = load_tec_model('data/TEC_COMSOL_results_full_grid.csv')

# Sweep across the range Jim's data actually covers
df = run_sweep(
    Qc_interp, Ptec_interp,
    I_range=np.linspace(7, 8.6, 20),      # stay within Jim's tested current range
    dT_range=np.linspace(0, 40, 15),       # stay within Jim's tested deltaT range
    T_in_range=[20, 30, 40],
    pr_range=[1.1, 1.2, 1.3, 1.4, 1.5]
)

df.to_csv('results/feasibility_sweep.csv', index=False)
print(f"Sweep complete: {len(df)} points saved to result/feasibility_sweep.csv")
print(df.head())
print(df.describe())