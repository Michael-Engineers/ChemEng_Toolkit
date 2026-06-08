from calculations.main_functions import functions, menu
from Utils.input_validation import get_integer



def main():
    print("****************************")
    print("Chemical Engineering Toolkit")
    print("****************************")

    while True:
        print("\nSelect Option")

        for key, value in menu.items():
            print(f"{key}. {value}")

        choice = get_integer()

        if choice not in functions:
            print("Please enter a valid option.")
            continue

        functions[choice]()

        if choice == 0:
            break


if __name__ == "__main__":
    main()