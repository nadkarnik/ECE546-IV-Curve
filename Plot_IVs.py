import numpy as np
import Unified_Model as UM
from matplotlib import pyplot as plt

plt.rcParams["figure.autolayout"] = True

def plot_curves(Vds, Vgs, intervalsToZero):
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



plot_curves(0.8, 0.8, 5)

plt.show()
