def build_profile(first: str, last: str, **user_info: str) -> dict:
    """
    Build a profile of a user based on what they input.

    :param first: User's first name (required).
    :param last: User's last name (required).
    :param user_info: Other information about the user, specified by keyword.

    :return: Dictionary of user information.
    """
    # It's crazy how this works!!
    user_info["first"] = first
    user_info["last"] = last
    return user_info

# Used for testing, but now we don't need these lines.
# user = build_profile("tony", "stark",
#                      location="california",
#                      occupation="iron man")
#
# print(user)