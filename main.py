from calculations.ideal_gas import run_ideal_gas
from calculations.arrhenius import run_arrhenius
from plotting.arrhenius_plot import run_arrhenius_plot
from plotting.ideal_gas_plot import run_ideal_gas_plot
from Utils.input_validation import get_integer


tools = {
    1: ("Ideal Gas Calculator", run_ideal_gas),
    2: ("Arrhenius Calculator", run_arrhenius),
    3: ("Ideal Gas Plotting", run_ideal_gas_plot),
    4: ("Arrhenius Plotting", run_arrhenius_plot),
    0: ("Exit", exit)
}


def print_menu():
    print("\n****************************")
    print("Chemical Engineering Toolkit")
    print("****************************\n")

    for key, (name, _) in tools.items():
        print(f"{key}. {name}")


def run_tool(choice):
    tools[choice][1]()


def main():
    while True:
        print_menu()

        choice = get_integer()

        if choice == 0:
            print("Exiting...")
            break

        if choice in tools:
            run_tool(choice)
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()