def make_car(make: str, model: str, **kwargs: str) -> dict:
    """
    Create a car based on the user's desired features.

    :param make: Manufacturer of the car (e.g. Honda, Ford).
    :param model: Model of the car (e.g. Civic, Explorer).
    :param kwargs: Other details about the car (e.g. luggage rack, color).

    :return: Dictionary describing the features of the car.
    """
    kwargs["make"] = make
    kwargs["model"] = model
    return kwargs


dream_car = make_car("mini", "cooper s",
                     color="british racing green",
                     roof="black",
                     turbo="True")
print(dream_car)