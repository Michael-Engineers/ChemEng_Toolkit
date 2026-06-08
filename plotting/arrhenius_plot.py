import matplotlib.pyplot as plt
import numpy as np

from Utils.input_validation import get_positive_float
from Utils.input_validation import get_integer

r = 8.314 #J/(K mol)

# K = A * e(-Ea/RT)


def plot_k_vs_t():
    ea = get_positive_float('Enter the activation energy (J/mol): ')
    a = get_positive_float('Enter the frequency factor: ')

    t_lower = get_positive_float("Enter lower temperature (K): ")
    t_upper = get_positive_float("Enter upper temperature (K): ")

    while t_upper <= t_lower:
        print("Upper temperature must be greater than lower temperature.")
        t_upper = get_positive_float("Enter upper temperature (K): ")

    t = np.linspace(t_lower, t_upper, 50)
    k = a * np.exp(-ea/(r*t))

    plt.plot(t, k)
    plt.xlabel("Temperature (K)")
    plt.ylabel("Reaction Rate Constant")
    plt.title(f"Reaction Rate Constant vs Temperature\nea={ea} J, a={a}")
    plt.grid(True)
    plt.show()


def run_arrhenius_plot():
    print("\n************")
    print("Arrhenius Plot")
    print("**************")

    print("1. K vs. T")


    choice = get_integer()

    if choice == 1:
        plot_k_vs_t()
    else:
        print("Invalid choice")