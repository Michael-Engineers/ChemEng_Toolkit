import matplotlib.pyplot as plt
import numpy as np

from Utils.input_validation import get_positive_float
from Utils.input_validation import get_integer

r = 8.314 #J/(K mol)

#PV = nRT
#p = nrt/v

def plot_p_vs_v():
    n = get_positive_float('Enter the number of moles:')
    t = get_positive_float('Enter the temperature (K):')
    v_lower = get_positive_float("Enter the lower range for volume (m^3):")
    v_upper = get_positive_float("Enter the upper range for volume (m^3):")
    while v_upper <= v_lower:
        print("Upper volume must be greater than lower volume.")
        v_upper = get_positive_float("Enter the upper range for volume (m^3):")
    v = np.linspace(v_lower, v_upper, num  = 50)
    p = (n*r*t/v)
    plt.plot(v,p)
    plt.xlabel("Volume (m^3)")
    plt.ylabel("Pressure (Pa)")
    plt.title("Pressure (Pa) vs Volume (m^3):\n"
              f"n = {n:.2f} mol, T = {t:.1f} K")
    plt.grid(True)
    plt.show()

def plot_p_vs_t():
    n = get_positive_float('Enter the number of moles:')
    v = get_positive_float('Enter the volume (m^3):')
    t_lower = get_positive_float("Enter the lower range for temperature (K):")
    t_upper = get_positive_float("Enter the upper range for temperature (K):")
    while t_upper <= t_lower:
        print("Upper Temperature must be greater than lower Temperature.")
        t_upper = get_positive_float("Enter the upper range for temperature (K):")
    t = np.linspace(t_lower, t_upper, num=50)
    p = (n * r * t / v)
    plt.plot(t, p)
    plt.xlabel("Temperature (K)")
    plt.ylabel("Pressure (Pa)")
    plt.title("Pressure (Pa) vs Temperature (K):\n"
              f"n = {n:.2f} mol, v = {v:.1f} m^3")
    plt.grid(True)
    plt.show()

def plot_v_vs_t():
    n = get_positive_float('Enter the number of moles:')
    p = get_positive_float('Enter the pressure (Pa):')
    t_lower = get_positive_float("Enter the lower range for temperature (K):")
    t_upper = get_positive_float("Enter the upper range for temperature (K):")
    while t_upper <= t_lower:
        print("Upper Temperature must be greater than lower Temperature.")
        t_upper = get_positive_float("Enter the upper range for temperature (K):")
    t = np.linspace(t_lower, t_upper, num=50)
    v = (n * r * t / p)
    plt.plot(t, v)
    plt.xlabel("Temperature (K)")
    plt.ylabel("Volume (m^3)")
    plt.title("Volume (m^3) vs Temperature (K):\n"
              f"n = {n:.2f} mol, p = {p:.1f} Pa")
    plt.grid(True)
    plt.show()


#Add in functionality to run it from the home screen
#Add in ideal_gas_plot function

options = {
    1: "Pressure vs. Volume",
    2: "Pressure vs. Temperature",
    3: "Volume vs. Temperature"
}

def run_ideal_gas_plot():
    print("\n********************")
    print("Ideal Gas Plotting Calculator")
    print("********************")

    for key, value in options.items():
        print(f"{key}. {value}")

    choice = get_integer()

    if choice not in options:
        print("Invalid choice")
        return

    match choice:
        case 1:
            plot_p_vs_v()
        case 2:
            plot_p_vs_t()
        case 3:
            plot_v_vs_t()