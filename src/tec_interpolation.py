import pandas as pd
import numpy as np
from scipy.interpolate import RegularGridInterpolator

def load_tec_model(csv_path):
    df = pd.read_csv(csv_path)

    df['Qc_abs'] = df['Qc_W'].abs()

    I_vals = np.sort(df['I_A'].unique())
    dT_vals = np.sort(df['DeltaT_K'].unique())

    print(f"Found {len(I_vals)} current values: {I_vals}")
    print(f"Found {len(dT_vals)} deltaT values: {dT_vals}")
    print(f"Expected grid size: {len(I_vals)*len(dT_vals)}, actual rows: {len(df)}")

    Qc_grid = df.pivot(index='I_A', columns='DeltaT_K', values='Qc_abs').values
    Ptec_grid = df.pivot(index='I_A', columns='DeltaT_K', values='PTEC_W').values

    Qc_interp = RegularGridInterpolator((I_vals, dT_vals), Qc_grid, bounds_error=False, fill_value=None)
    Ptec_interp = RegularGridInterpolator((I_vals, dT_vals), Ptec_grid, bounds_error=False, fill_value=None)

    return Qc_interp, Ptec_interp
