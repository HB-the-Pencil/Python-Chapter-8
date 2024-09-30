def make_shirt(size: str, message: str):
    """
    Function that accepts the size of a shirt and message to put on the shirt
    and then prints out an order summary.

    :param size: Size of the shirt (xs, s, m, l, xl, etc).
    :param message: Message to put on the shirt.

    :return: Prints "You ordered a {size} shirt that says {message} on the
        front."
    """

    print(f'You ordered a size {size.upper()} shirt that says "{message}" on '
          f'the front.')

make_shirt("xs", "This is my tiny shirt. It's tiny.")
make_shirt(message="Message before size. oh yeah", size="l")