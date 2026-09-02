import CoolProp.CoolProp as CP

P_ATM = 101325  # Pa

def get_T_sat(pressure_ratio):
    P = pressure_ratio * P_ATM
    T_sat_K = CP.PropsSI('T', 'P', P, 'Q', 0, 'Water')
    return T_sat_K - 273.15
if __name__ == "__main__":
    print(get_T_sat(1.2))
    