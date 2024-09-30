def favorite_book(title: str):
    """
    Function to print a neatly formatted statement of the user's favorite
    book.

    :param title: Title of the book.

    :return: Prints "My favorite book is {title}."
    """

    print(f"My favorite book is {title.title()}.")

book = input("Input the name of your favorite book. > ").lower().strip()
favorite_book(book)