"""Helper functions for the cafe bill program."""

# These are the fixed prices for each item in the cafe.
COFFEE_PRICE = 8.50
TEA_PRICE = 6.00
SANDWICH_PRICE = 12.00


def calculate_total(coffee, tea, sandwich):
    """Calculate the total bill using the quantity of each item."""
    # Multiply each quantity by its price.
    coffee_total = coffee * COFFEE_PRICE
    tea_total = tea * TEA_PRICE
    sandwich_total = sandwich * SANDWICH_PRICE

    # Add all item totals together to get the final bill.
    total = coffee_total + tea_total + sandwich_total
    return total


def print_receipt(customer_name, coffee, tea, sandwich, total):
    """Print a simple receipt for the customer."""
    # This part displays the customer's order and the final total.
    print("\n===== RECEIPT =====")
    print(f"Customer : {customer_name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print("-------------------")
    print(f"Total = RM {total:.2f}")
