from calculations.ideal_gas import ideal_gas_moles
from calculations.ideal_gas import ideal_gas_pressure
from calculations.ideal_gas import ideal_gas_volume
from calculations.ideal_gas import ideal_gas_temperature


def run_ideal_gas():
    print("********************")
    print("Ideal Gas Calculator")
    print("********************")

    print("0. Exit")
    print("1. Calculate Moles")
    print("2. Calculate Pressure")
    print("3. Calculate Volume")
    print("4. Calculate Temperature")

    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("Please enter a choice from the list")
        choice = int(input("Enter your choice:"))

    match choice:
        case 1: #Moles
            p = float(input("Pressure (Pa): "))
            v = float(input("Volume (m^3): "))
            t = float(input("Temperature (K): "))
            n = ideal_gas_moles(p,v,t)
            print(f"\nMoles of gas: {n:.4f} mol\n")
        case 2: #Pressure
            n = float(input("Moles: "))
            v = float(input("Volume (m^3): "))
            t = float(input("Temperature (K): "))
            p = ideal_gas_pressure(n,v,t)
            print(f"\nPressure of gas: {p:.4f} Pa\n")
        case 3:  #Volume
            p = float(input("Pressure (Pa): "))
            n = float(input("Moles: "))
            t = float(input("Temperature (K): "))
            v = ideal_gas_volume(p,t,n)
            print(f"\nVolume of gas: {v:.4f} m^3\n")
        case 4:  #Temperature
            p = float(input("Pressure (Pa): "))
            n = float(input("Moles: "))
            v = float(input("Volume (m^3): "))
            t = ideal_gas_temperature(p,v,n)
            print(f"\nTemperature of Gas: {t:.4f} K\n")
        case _:
            print("Please enter a choice from the list")

    choice = int(input("Enter your choice:"))




def main():
    print("****************************")
    print("Chemical Engineering Toolkit")
    print("****************************")
    print("Select Option")
    print("1. Ideal Gas Calculator")
    print("0. Exit")

    while True:
        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("Please enter a choice from the list")
            choice = int(input("Enter your choice:"))

        match choice:
            case 1:
                run_ideal_gas()
            case _:
                print("Please enter a choice from the list")



if __name__ == "__main__":
    main()

