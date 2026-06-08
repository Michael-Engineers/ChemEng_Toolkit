import matplotlib.pyplot as plt
import numpy as np

from Utils.input_validation import get_positive_float
from Utils.input_validation import get_integer

r = 8.314


def plot_p_vs_v():
    n = get_positive_float('Enter the number of moles: ')
    t = get_positive_float('Enter the temperature (K): ')

    v_lower = get_positive_float("Enter lower volume (m^3): ")
    v_upper = get_positive_float("Enter upper volume (m^3): ")

    while v_upper <= v_lower:
        print("Upper volume must be greater than lower volume.")
        v_upper = get_positive_float("Enter upper volume (m^3): ")

    v = np.linspace(v_lower, v_upper, 50)
    p = (n * r * t) / v

    plt.plot(v, p)
    plt.xlabel("Volume (m^3)")
    plt.ylabel("Pressure (Pa)")
    plt.title(f"Pressure vs Volume\nn={n} mol, T={t} K")
    plt.grid(True)
    plt.show()


def plot_p_vs_t():
    n = get_positive_float('Enter the number of moles: ')
    v = get_positive_float('Enter the volume (m^3): ')

    t_lower = get_positive_float("Enter lower temperature (K): ")
    t_upper = get_positive_float("Enter upper temperature (K): ")

    while t_upper <= t_lower:
        print("Upper temperature must be greater than lower temperature.")
        t_upper = get_positive_float("Enter upper temperature (K): ")

    t = np.linspace(t_lower, t_upper, 50)
    p = (n * r * t) / v

    plt.plot(t, p)
    plt.xlabel("Temperature (K)")
    plt.ylabel("Pressure (Pa)")
    plt.title(f"Pressure vs Temperature\nn={n} mol, V={v} m^3")
    plt.grid(True)
    plt.show()


def plot_v_vs_t():
    n = get_positive_float('Enter the number of moles: ')
    p = get_positive_float('Enter the pressure (Pa): ')

    t_lower = get_positive_float("Enter lower temperature (K): ")
    t_upper = get_positive_float("Enter upper temperature (K): ")

    while t_upper <= t_lower:
        print("Upper temperature must be greater than lower temperature.")
        t_upper = get_positive_float("Enter upper temperature (K): ")

    t = np.linspace(t_lower, t_upper, 50)
    v = (n * r * t) / p

    plt.plot(t, v)
    plt.xlabel("Temperature (K)")
    plt.ylabel("Volume (m^3)")
    plt.title(f"Volume vs Temperature\nn={n} mol, P={p} Pa")
    plt.grid(True)
    plt.show()


def run_ideal_gas_plot():
    print("\n********************")
    print("Ideal Gas Plotting Calculator")
    print("********************")

    print("1. Pressure vs Volume")
    print("2. Pressure vs Temperature")
    print("3. Volume vs Temperature")

    choice = get_integer()

    if choice == 1:
        plot_p_vs_v()
    elif choice == 2:
        plot_p_vs_t()
    elif choice == 3:
        plot_v_vs_t()
    else:
        print("Invalid choice")