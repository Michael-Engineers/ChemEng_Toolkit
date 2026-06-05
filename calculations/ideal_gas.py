# PV = nRT

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

    from Utils.input_validation import get_integer
    choice = get_integer()

    if choice not in options:
        print("Invalid choice")
        return

    if choice == 1:
        p = float(input("Pressure (Pa): "))
        v = float(input("Volume (m^3): "))
        t = float(input("Temperature (K): "))
        n = ideal_gas_moles(p, v, t)
        print(f"\nMoles of gas: {n:.4f} mol\n")

    elif choice == 2:
        n = float(input("Moles: "))
        v = float(input("Volume (m^3): "))
        t = float(input("Temperature (K): "))
        p = ideal_gas_pressure(n, v, t)
        print(f"\nPressure of gas: {p:.4f} Pa\n")

    elif choice == 3:
        p = float(input("Pressure (Pa): "))
        n = float(input("Moles: "))
        t = float(input("Temperature (K): "))
        v = ideal_gas_volume(p, t, n)
        print(f"\nVolume of gas: {v:.4f} m^3\n")

    elif choice == 4:
        p = float(input("Pressure (Pa): "))
        v = float(input("Volume (m^3): "))
        n = float(input("Moles: "))
        t = ideal_gas_temperature(p, v, n)
        print(f"\nTemperature of gas: {t:.4f} K\n")