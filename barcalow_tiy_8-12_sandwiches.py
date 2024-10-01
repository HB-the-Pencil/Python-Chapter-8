def order_sandwich(*args: str):
    """
    Create a sandwich order for a user.

    :param args: Topping(s) for the sandwich.

    :return: Prints a receipt for your order.
    """
    print("=== Your Order ===")
    print("You ordered a sandwich with the following toppings:")
    for topping in args:
        print("  -", topping)
    print()


order_sandwich("pastrami", "mustard")
order_sandwich("peanut butter", "grape jelly", "potato chips")
order_sandwich("turkey breast", "bacon", "mustard", "pickles", "cheese")