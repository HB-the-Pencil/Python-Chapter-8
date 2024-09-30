def make_album(title: str, artist: str, length: int = None) -> dict:
    """
    Create a dictionary describing an album, including the title, artist, and
    length.

    :param title: Title of the album.
    :param artist: Artist who recorded the album.
    :param length: Number of songs in the album, if specified.

    :return: Dictionary containing keys "title", "artist", and "length" which
        correspond to the input data.
    """

    album = {"title": title, "artist": artist}

    # If length is defined, add it to the album.
    if length:
        album["length"] = length

    return album

# Define four albums.
j_escape = make_album("Escape", "Journey")
q_opera = make_album("A Night at the Opera", "Queen")
c_shake = make_album("Shake It Up", "The Cars")
r_2112 = make_album("2112", "Rush", 12)

# Print information about said albums.
print(j_escape)
print(q_opera)
print(c_shake)
print(r_2112)