

def get_integer():
        while True:
            try:
                return int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid integer.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_positive_float(prompt):
    while True:
        try:
             data = float(input(prompt))
             if data <= 0:
                 print("Please enter a positive number.")
             else:
                 return data
        except ValueError:
            print("Please enter a valid number.")