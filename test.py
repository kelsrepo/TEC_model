from src.tec_interpolation import load_tec_model
from src.energy_balance import solve_operating_point

Qc_interp, Ptec_interp = load_tec_model('data/TEC_COMSOL_results_full_grid.csv')

# Test at a point that exists directly in the CSV: I=8.1, deltaT=20
result = solve_operating_point(I=8.1, deltaT=20, T_in=20.0, pressure_ratio=1.2,
                                Qc_interp=Qc_interp, Ptec_interp=Ptec_interp)
print(result)