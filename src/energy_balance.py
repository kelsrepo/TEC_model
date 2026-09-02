from src.water_properties import get_T_sat

def solve_operating_point(I, deltaT, T_in, pressure_ratio, Qc_interp, Ptec_interp):
    Qc = float(Qc_interp([[I, deltaT]])[0])
    Ptec = float(Ptec_interp([[I, deltaT]])[0])
    Qh = Qc + Ptec

    T_sat = get_T_sat(pressure_ratio)
    cp = 4186

    m_dot_required = Qh / (cp * (T_sat - T_in))

    return {
        'I': I, 'deltaT': deltaT, 'T_in': T_in, 'pressure_ratio': pressure_ratio,
        'Qc': Qc, 'Ptec': Ptec, 'Qh': Qh,
        'T_sat': T_sat, 'm_dot_required': m_dot_required, 'COP': Qc / Ptec
    }