def city_country(city: str, country: str) -> str:
    """
    Return the name of a city and the country it is in.

    :param city: Name of the city.
    :param country: Country in which the city is located.

    :return: String "{city}, {country}"
    """
    location = f"{city.title()}, {country.title()}"
    return location

print(city_country("fort wayne", "united states"))
print(city_country("santiago", "chile"))
print(city_country("london", "england"))