# Drag-Force Calculation & Visualization 🏍️💨

This repository contains **GNU Octave/MATLAB** scripts designed to calculate and visualize the aerodynamic drag force experienced by a vehicle (specifically modeled after a **Bajaj CT100** motorcycle) at various speeds.

It demonstrates the exponential relationship between velocity and air resistance using standard fluid dynamics equations.

## 📂 File Structure

* **`dragf.m`** The core function file. It accepts velocity (in km/h) as an input and returns the calculated Drag Force ($F_d$) in Newtons.
    
* **`dragG.m`** The plotting script. It generates a graph (Velocity vs. Drag Force) to visualize how air resistance increases non-linearly as speed increases.

## 🧮 The Physics

The scripts use the standard Drag Equation:

$$F_d = \frac{1}{2} \rho v^2 C_d A$$

Where:
* **$F_d$**: Drag Force (Newtons)
* **$\rho$ (rho)**: Air Density ($\approx 1.225 \, kg/m^3$)
* **$v$**: Velocity (converted to $m/s$)
* **$C_d$**: Drag Coefficient (Dimensionless, based on shape)
* **$A$**: Frontal Area ($m^2$)

## 🚀 How to Run

1.  Ensure you have **GNU Octave** or **MATLAB** installed.
2.  Clone this repository or download the files.
3.  Open your terminal/command window in the folder containing these files.

### To calculate force for a specific speed:
```matlab
>> dragf(45)
% Returns the force in Newtons at 45 km/h
