import time
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation

def dragf(fa, rho, v, cd):
    return 0.5 * rho * (v**2) * fa * cd

# Constants
v_kmh = 60
rho = 1.1950
cd = 0.35
fa = 1.955

# Single calculation
v_ms = v_kmh * (5/18)
fd_single = dragf(fa, rho, v_ms, cd)
print(f"Drag Force for {v_kmh} km/h = {fd_single:.3f} N")

# Data for plotting
v_kmh_plot = np.arange(0,120, 1)  # 0 to 700 inclusive
v_ms_plot = v_kmh_plot * (5/18)
fd_zen_car = dragf(fa, rho, v_ms_plot, cd)
fd_person=dragf(0.6194,1.168,v_ms_plot,1.15)
for i in range(0,120):
    v_kmh_plot_for = np.arange(0,i, 1)  # 0 to 700 inclusive
    v_ms_plot_for = v_kmh_plot_for * (5/18)
    fd_nigga=dragf(0.6194,1.168,v_ms_plot_for,1.15)
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(fd_zen_car, v_kmh_plot, linewidth=2)
#plt.plot(fd_person, v_kmh_plot, linewidth=2)
plt.plot(fd_nigga, v_kmh_plot_for, linewidth=2)
plt.grid(True)
plt.xlabel("Drag Force (N)")
plt.ylabel("Speed (km/h)")
plt.title("Drag Force vs Speed")
plt.show()