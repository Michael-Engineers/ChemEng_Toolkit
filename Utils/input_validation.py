from calculations.ideal_gas import options


def get_integer():
        while True:
            try:
                return int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid integer.")