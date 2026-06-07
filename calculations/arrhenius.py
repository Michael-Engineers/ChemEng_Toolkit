import math

# K = Ae^(-Ea/RT)
r = 8.314 #J/(K Mol)

from Utils.input_validation import get_integer
from Utils.input_validation import get_positive_float



options = {
    1: "Calculate Rate Constant (K)",
    2: "Calculate Activation Energy (Ea)",
    3: "Calculate Frequency Factor (A)",
    4: "Calculate Temperature (T)"
}

def arrhenius_rate_constant(a,ea,t):
    return a*math.exp(-ea/(r*t))
def arrhenius_activation_energy(a,k,t):
    return r*t*math.log(a/k)
def arrhenius_frequency_factor(ea,k,t):
    return k * math.exp(ea/(r*t))
def arrhenius_temperature(a,ea,k):
    return -ea/(r * math.log(k/a))

def run_arrhenius():
    print("\n********************")
    print("Arrhenius Equation Calculator")
    print("********************")

    for key, value in options.items():
        print(f"{key}. {value}")

    choice = get_integer()

    if choice not in options:
        print("Invalid choice")
        return

    if choice == 1:
        a = get_positive_float("Frequency Factor (A): ")
        ea = get_positive_float("Activation Energy (J/mol): ")
        t = get_positive_float("Temperature (K): ")
        k = arrhenius_rate_constant(a,ea,t)
        print(f"\nRate Constant: {k:.4f} \n")

    elif choice == 2:
        a = get_positive_float("Frequency Factor (A): ")
        t = get_positive_float("Temperature (K): ")
        k = get_positive_float("Reaction Rate Constant:")
        ea = arrhenius_activation_energy(a,k,t)
        print(f"\nActivation Energy: {ea:.4f} \n")

    elif choice == 3:
        ea = get_positive_float("Activation Energy (J/mol): ")
        t = get_positive_float("Temperature (K): ")
        k = get_positive_float("Reaction Rate Constant:")
        a = arrhenius_frequency_factor(ea,k,t)
        print(f"\nFrequency Factor: {a:.4f} \n")

    elif choice == 4:
        a = get_positive_float("Frequency Factor (A): ")
        ea = get_positive_float("Activation Energy (J/mol): ")
        k = get_positive_float("Reaction Rate Constant:")
        t = arrhenius_temperature(a,ea,k)
        print(f"\nTemperature: {t:.4f} \n")