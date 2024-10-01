def build_profile(first: str, last: str, **user_info: str) -> dict:
    """
    Build a profile of a user based on what they input.

    :param first: User's first name (required).
    :param last: User's last name (required).
    :param user_info: Other information about the user, specified by keyword.

    :return: Dictionary of user information.
    """
    user_info["first"] = first
    user_info["last"] = last
    return user_info


myself = build_profile("henry", "barcalow",
                       age="16",
                       favorite_food="steak",
                       favorite_thing="rockin")

# This tells you enough about me... massive nerd.
print(myself)