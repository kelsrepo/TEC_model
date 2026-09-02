import pandas as pd
from src.tec_interpolation import load_tec_model
from src.energy_balance import solve_operating_point

raw = pd.read_csv('data/TEC_COMSOL_results_full_grid.csv')
Qc_interp, Ptec_interp = load_tec_model('data/TEC_COMSOL_results_full_grid.csv')

print(f"{'I':>6} {'dT':>6} {'Model Qh':>10} {'COMSOL Qh':>10} {'Error %':>8}")
for _, row in raw.iterrows():
    result = solve_operating_point(row['I_A'], row['DeltaT_K'], T_in=20, pressure_ratio=1.2,
                                    Qc_interp=Qc_interp, Ptec_interp=Ptec_interp)
    error = 100 * (result['Qh'] - row['Qh_W']) / row['Qh_W']
    print(f"{row['I_A']:>6} {row['DeltaT_K']:>6} {result['Qh']:>10.4f} {row['Qh_W']:>10.4f} {error:>8.2f}")