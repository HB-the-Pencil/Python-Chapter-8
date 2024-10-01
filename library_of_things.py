""" The most recent version of my library. It's no longer just a grammar
library.

Don't worry, there will still be try-except cases whenever this is used. I
will also be removing any unit tests I use before I turn in the assignments.
"""


def add_article(word:str) -> str:
    """
    Add an article adjective (a or an) to a word. Very basic.

    :param word: The word which needs an article.

    :return: String including an article and the word.

    Example:
        add_article("elephant")

        Returns "an elephant"
    """
    # Define a list of vowels.
    vowels = ["a", "e", "i", "o", "u"]

    # Return "an" + the word if it starts with a vowel; else, "a" + the word.
    if word[:1] in vowels:
        return f"an {word}"
    else:
        return f"a {word}"


def punctuate_list(list_of_items:list, title:bool=False,
                   conjunction:str="and", ending:str=".") -> str:
    """
    Punctuate a list of items as a sentence.

    :param list_of_items: List of items to be punctuated.
    :param title: Whether to capitalize the items or not (False by
        default).
    :param conjunction: Conjunction to use at the end of the list ("and" by
        default). Think FANBOYS.
    :param ending: End of the sentence ("." by default). Generally, the
        ending will be a period (possibly with a newline) or a space.

    :return: String version of the list with commas after each item. If the
        list contains 0 items, returns "Nothing in list."

    Example:
        punctuate_list(["foo", "bar", "baz"], False, "and", "!")

        Returns "foo, bar, and baz!"
    """
    # If the list of items isn't a list, make it one.
    if not isinstance(list_of_items, list):
        list_of_items = list(list_of_items)

    # Convert all items into strings so they can be concatenated.
    items = [str(item) for item in list_of_items]
    message = ""

    # If the list is empty, print that the list is empty.
    if len(items) == 0:
        return "Nothing in list."

    # Loop through the list.
    for i in range(len(items)):

        # Define the item. I had to rewrite because .index() only finds the
        # first occurrence.
        item = items[i]

        # If it's before the next-to-last place, add a comma to the end.
        if i < len(items) - 2:
            if title:
                message += f"{item.title()}, "
            else:
                message += f"{item}, "

        # If it's the next to last place, add "and".
        elif i < len(items) - 1:
            # Omit the comma if the list length is two.
            if len(items) == 2:
                if title:
                    message += f"{item.title()} {conjunction} "
                else:
                    message += f"{item} {conjunction} "
            else:
                if title:
                    message += f"{item.title()}, {conjunction} "
                else:
                    message += f"{item}, {conjunction} "

        # If it's the last place, add a period and a newline.
        else:
            if title:
                message += f"{item.title()}{ending}"
            else:
                message += f"{item}{ending}"

    # Return the message.
    return message


def c_input(prompt:str) -> str:
    """
    Clean an input by stripping it and making it lowercase.

    :param prompt: The prompt text for the input.

    :return: The user's cleaned input.

    Example:
          c_input("What is your name? ")
          <User inputs " Archibald   ">
          Returns "archibald"
    """
    return input(prompt).strip().lower()


def unit_test(i_o:dict) -> list:
    """
    Perform unit tests by comparing a dictionary of inputs and outputs.

    :param i_o: Dictionary of inputs (keys) and outputs (values).

    :return: List of the results from each test. Also prints out a debugging
        statement when a test fails.

    Example:
        unit_test({sum([4, 5, 6]): 15, "bee": "Bee"})

        Returns [True, False].
        Prints "Unexpected output found at item 1!"
        Prints "    Expected: Bee"
        Prints "    Actual: bee"
    """
    # Create a results list and test each value.
    results = []
    for input_val, output_val in i_o.items():
        results.append(input_val == output_val)

        # Print a message if a value is unexpected.
        if not input_val == output_val:
            print(f"Unexpected output found at item {len(results)-1}!")
            print(f"\tExpected: {output_val}")
            print(f"\tActual: {input_val}\n")

    # Return the results.
    return results