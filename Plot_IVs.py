import numpy as np
import Unified_Model as UM
from matplotlib import pyplot as plt

plt.rcParams["figure.autolayout"] = True

def plot_curves_nmos(Vds, Vgs, intervalsToZero):
    x_scale = np.linspace(0, Vds, 50)
    vds_voltages = x_scale
    vgs_voltages = np.linspace(0, Vgs, intervalsToZero)
    for j, vgs_val in enumerate(vgs_voltages):
        currents = [0] * len(vds_voltages)
        for i, vds_val in enumerate(vds_voltages):
            currents[i] = UM.calc_drain_current_nmos(vgs_val,0.2,52,15,vds_val)
        vds_voltages = x_scale
        plt.plot(vds_voltages, currents, color='red')
        plt.text(Vds, currents[-1], 'Vgs Voltage: '+str(vgs_val), fontsize=12)
    return 

## Remember that Vgs and Vds for PMOS are positive values w.r.t Vdd & GND
## Example Usage: plot_curves_nmos(0.8, 0.8, 5)



def plot_curves_pmos(Vds, Vgs, intervalsToZero):
    x_scale = np.linspace(0, Vds, 50)
    vds_voltages = x_scale
    vgs_voltages = np.linspace(0, Vgs, intervalsToZero)
    for j, vgs_val in enumerate(vgs_voltages):
        currents = [0] * len(vds_voltages)
        for i, vds_val in enumerate(vds_voltages):
            currents[i] = UM.calc_drain_current_pmos(vgs_val,0.2,104,15,vds_val)
        vds_voltages = x_scale
        plt.plot(vds_voltages, currents, color='red')
        plt.text(Vds, currents[-1], 'Vgs Voltage: '+str(vgs_val), fontsize=12)
    return 


## Remember that Vgs and Vds for PMOS are negative values w.r.t Vdd & GND
## Example Usage: plot_curves_pmos(-0.8, -0.8, 5)


def show_plot():
    plt.show()    

## Example Usage: show_plot()



