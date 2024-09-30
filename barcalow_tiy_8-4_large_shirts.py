def make_shirt(size: str = "L", message: str = 'print("I <3 Python")'):
    """
    Modified version of the make_shirt function that sets the size to L and
    the message to 'print("I <3 Python")' by default.

    :param size: Size of the shirt (xs, s, m, l, xl, etc).
    :param message: Message to put on the shirt.

    :return: Prints "You ordered a {size} shirt that says {message} on the
        front."
    """

    print(f'You ordered a size {size.upper()} shirt that says "{message}" on '
          f'the front.')

make_shirt()
make_shirt(size="m")
make_shirt(size="xl", message="Python is for babies; Java for life;")