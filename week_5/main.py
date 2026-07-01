"""Main program for the cafe bill calculator."""

from utils import calculate_total, print_receipt


def get_customer_name():
    """Ask the user to enter a customer name."""
    while True:
        name = input("Customer name: ").strip()

        # The name must not be empty.
        if name:
            return name

        print("Customer name cannot be empty. Please try again.")


def get_quantity(item_name):
    """Ask the user to enter a valid item quantity."""
    while True:
        user_input = input(f"{item_name} quantity: ").strip()

        try:
            # Convert the user's input into a whole number.
            quantity = int(user_input)

            # Quantity cannot be less than zero.
            if quantity < 0:
                print("Quantity cannot be negative. Please enter 0 or more.")
            else:
                return quantity

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    """Run the cafe bill calculator."""
    print("Cafe Bill Calculator")
    print("--------------------")

    # Get the customer details and order quantities.
    customer_name = get_customer_name()
    coffee = get_quantity("Coffee")
    tea = get_quantity("Tea")
    sandwich = get_quantity("Sandwich")

    # Calculate the bill and print the receipt.
    total = calculate_total(coffee, tea, sandwich)
    print_receipt(customer_name, coffee, tea, sandwich, total)


if __name__ == "__main__":
    main()
