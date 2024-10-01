def print_models(designs: list, completed_models: list):
    """
    Loop through a list of designs and move them to a list of
    printed designs.

    :param designs: The designs that have yet to be printed.
    :param completed_models: The designs that have been printed.

    :return: Prints out a statement for each item that has been "printed"
        and fills the completed_models list with the items from the designs
        list.
    """
    while designs:
        # Pop at 0 so that the list goes in the fill order.
        current = designs.pop(0)
        print(f"Printing model {current}")
        print("...")
        completed_models.append(current)
        print(f"Model {current} completed\n")


def show_completed(printed: list):
    """
    Print a list of the items that have been printed.

    :param printed: List of items that have been printed.

    :return: Prints a punctuated list of items (if library of things has been
        imported) or a bulleted list of items.
    """
    print("Printed models:")
    for model in printed:
       print("  -", model)