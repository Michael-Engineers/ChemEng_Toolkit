# PV = nRT
from Utils.input_validation import get_integer
from Utils.input_validation import get_positive_float

r = 8.314  # J/(mol·K)

options = {
    1: "Calculate Moles",
    2: "Calculate Pressure",
    3: "Calculate Volume",
    4: "Calculate Temperature"
}

def ideal_gas_moles(p, v, t):
    return (p * v) / (r * t)

def ideal_gas_pressure(n, v, t):
    return (n * r * t) / v

def ideal_gas_volume(p, t, n):
    return (n * r * t) / p

def ideal_gas_temperature(p, v, n):
    return (p * v) / (r * n)


def run_ideal_gas():
    print("\n********************")
    print("Ideal Gas Calculator")
    print("********************")

    for key, value in options.items():
        print(f"{key}. {value}")

    choice = get_integer()

    if choice not in options:
        print("Invalid choice")
        return

    if choice == 1:
        p = get_positive_float("Pressure (Pa): ")
        v = get_positive_float("Volume (m^3): ")
        t = get_positive_float("Temperature (K): ")
        n = ideal_gas_moles(p, v, t)
        print(f"\nMoles of gas: {n:.4f} mol\n")

    elif choice == 2:
        n = get_positive_float("Moles")
        v = get_positive_float("Volume (m^3): ")
        t = get_positive_float("Temperature (K): ")
        p = ideal_gas_pressure(n, v, t)
        print(f"\nPressure of gas: {p:.4f} Pa\n")

    elif choice == 3:
        p = get_positive_float("Pressure (Pa): ")
        n = get_positive_float("Moles: ")
        t = get_positive_float("Temperature (K): ")
        v = ideal_gas_volume(p, t, n)
        print(f"\nVolume of gas: {v:.4f} m^3\n")

    elif choice == 4:
        p = get_positive_float("Pressure (Pa): ")
        v = get_positive_float("Volume (m^3): ")
        n = get_positive_float("Moles: ")
        t = ideal_gas_temperature(p, v, n)
        print(f"\nTemperature of gas: {t:.4f} K\n")