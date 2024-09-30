def describe_city(city: str, country: str = "United States"):
    """
    Function that prints the name of a city and its corresponding country.

    :param city: Name of the city.
    :param country: Country in which the city is located ("United States" by
        default, since that's where I made the program).

    :return: Prints "{city} is in {country}."
    """

    print(f"{city.title()} is in {country.title()}.")

describe_city("fort wayne")
describe_city("sarnia", "canada")
describe_city("quito", "ecuador")