import pandas as pd



def create_transistor_lookup(voltage_table, capacitance_table, default=None):
    """
    Creates a lookup function for transistor design calculations using exact voltage matching.
    
    Args:
        voltage_table (pd.DataFrame): Table with voltage types as columns and transition times as rows
        capacitance_table (pd.DataFrame): Table with voltages as columns and C_ov values
        default: Value to return when voltage isn't found (default: None)
        
    Returns:
        function: Takes voltage type (column name) and returns corresponding C_ov values
    """
    # Convert capacitance table columns to numeric values
    capacitance_table.columns = pd.to_numeric(capacitance_table.columns, errors='coerce')
    
    # Create lookup dictionaries
    voltage_dict = voltage_table.to_dict(orient="list")
    capacitance_dict = capacitance_table.iloc[0].to_dict()

    def lookup(voltage_type):
        # Get voltages for requested type
        voltages = voltage_dict.get(voltage_type)
        if not voltages:
            raise ValueError(f"Voltage type '{voltage_type}' not found in voltage table")
            
        # Get corresponding capacitances
        return [capacitance_dict.get(voltage, default) for voltage in voltages]

    return lookup



def calc_drain_current_nmos(Vgs, Vt0, Width, Length, Vds):
    drain_current = 0
    Vdsat=0.11
    Vt=Vt0-0.02*Vds                 #Vt0n is typically 0.2
    Vmin=min(Vdsat, Vds, Vgs-Vt)
    Kprime=420*(10**(-6))
    LambdaParam=0.02

    if (Vgs-Vt)<=0:
        drain_current=0
    elif (Vgs-Vt)>0:
        drain_current=Kprime*Width/Length*(((Vgs-Vt)*Vmin)-(Vmin**2)/2)*(1+LambdaParam*Vds)
    return drain_current

def calc_drain_current_pmos(Vgs, Vt0, Width, Length, Vds):
    drain_current = 0
    Vdsat=-0.11
    Vt=Vt0-0.04*Vds                 #Vt0p is typically 0.2
    Vmin=min(Vdsat, Vds, Vgs-Vt, key=abs)
    Kprime=-340*(10**(-6))
    LambdaParam=-0.15

    if (Vgs-Vt)>=0:
        drain_current=0
    elif (Vgs-Vt)<0:
        drain_current=Kprime*Width/Length*(((Vgs-Vt)*Vmin)-(Vmin**2)/2)*(1+LambdaParam*Vds)
    return drain_current


def calc_Req_n(Vdd):
    Id_nmos_fullVdd=calc_drain_current_nmos(Vdd,0.2,52,15,Vdd)
    Id_nmos_halfVdd=calc_drain_current_nmos(Vdd,0.2,52,15,Vdd*0.5)

    Req_n=0.5*(Vdd/Id_nmos_fullVdd+0.5*Vdd/Id_nmos_halfVdd)
    return Req_n

def calc_Req_p(Vdd):
    Id_pmos_fullVdd=calc_drain_current_pmos(-Vdd,-0.2,52,15,-Vdd)
    Id_pmos_halfVdd=calc_drain_current_pmos(-Vdd,-0.2,52,15,-Vdd*0.5)
    Req_p=0.5*(Vdd/Id_pmos_fullVdd+0.5*Vdd/Id_pmos_halfVdd)
    return abs(Req_p)    

def average_capacitance(capacitances):
    if 'N/A' not in capacitances:
        return sum(capacitances)/len(capacitances)
    else: 
        capacitances.remove('N/A')
        return sum(capacitances)/len(capacitances)




##print(calc_drain_current_pmos(-0.8, -0.2, 52, 15, -0.4))
##print(calc_Req_n(0.8))
##print(calc_Req_p(0.8))