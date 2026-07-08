"""Logic functions for the FoodExpress food order system."""


def calculate_total(price, quantity):
    """Calculate the total payment for a food order."""
    # The price must be a number and must be more than zero.
    if not isinstance(price, (int, float)) or isinstance(price, bool) or price <= 0:
        return "invalid price"

    # The quantity must be a whole number and must be more than zero.
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        return "invalid quantity"

    return price * quantity


# This name is added because the tutorial test template uses food_order().
food_order = calculate_total
