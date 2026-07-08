"""Main program for Week 7 food order calculator."""

from food_order import calculate_total


def get_price():
    """Ask the user to enter a valid food price."""
    while True:
        try:
            price = float(input("Price (RM): "))

            # Price must be more than zero because food cannot have a negative price.
            if calculate_total(price, 1) == "invalid price":
                print("Invalid price. Please enter a price more than 0.")
            else:
                return price

        except ValueError:
            print("Invalid price. Please enter numbers only.")


def get_quantity():
    """Ask the user to enter a valid food quantity."""
    while True:
        try:
            quantity = int(input("Quantity: "))

            # Quantity must be a whole number more than zero.
            if calculate_total(1, quantity) == "invalid quantity":
                print("Invalid quantity. Please enter a quantity more than 0.")
            else:
                return quantity

        except ValueError:
            print("Invalid quantity. Please enter a whole number only.")


def main():
    """Run the food order calculator."""
    price = get_price()
    quantity = get_quantity()

    total = calculate_total(price, quantity)

    print(f"Total Payment = RM {total:.2f}")


if __name__ == "__main__":
    main()
