import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('results/feasibility_sweep.csv')

# COP vs current and deltaT, at one fixed T_in / pressure ratio
subset = df[(df['T_in'] == 20) & (df['pressure_ratio'] == 1.2)]
pivot = subset.pivot_table(values='COP', index='deltaT', columns='I')

plt.figure(figsize=(8, 6))
cs = plt.contourf(pivot.columns, pivot.index, pivot.values, levels=20, cmap='viridis')
plt.colorbar(cs, label='COP')
plt.xlabel('TEC current (A)')
plt.ylabel('ΔT (K)')
plt.title('Feasibility map: COP vs. current and ΔT\n(T_in=20°C, pressure ratio=1.2)')
plt.tight_layout()
plt.savefig('results/feasibility_map.png', dpi=150)
plt.show()
print("Saved results/feasibility_map.png")