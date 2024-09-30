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

    created_album = {"title": title, "artist": artist}

    # If length is defined, add it to the album.
    if length:
        created_album["length"] = length

    return created_album


# Their version is rather bland. I want to try making a list that the albums
# are passed into.
playlist = []

# I also wanted to make it so you could just pick one song, not a whole album,
# but let's not go too crazy.

print("-= Playlist Creation Tool =-\n")

while True:
    print("Enter information about albums to create a playlist. Type QUIT "
          "at any time to quit.")

    # Get the data.
    album_title = input("Name of the album: ").strip()
    if album_title == "quit":
        break

    album_artist = input("Artist/Group who recorded the album: ").strip()
    if album_artist == "quit":
        break

    album_length = input("Album length (whole number or leave empty): ")
    if album_length == "quit":
        break

    # If the user left the length empty, assign it to None to avoid errors.
    if album_length == "":
        album_length = None

    # Try to accept an integer for the album length.
    try:
        album_length = int(album_length)

        # An album can't have negative or zero length, so if it does, raise
        # a value error.
        if album_length < 1:
            raise ValueError

    except (ValueError, TypeError):
        # If the user left length empty, it should be None already and should
        # not throw an error.
        if album_length is not None:
            print("Error in album length input (not an integer).")
            album_length = None

    # Add the album to the user's playlist.
    playlist.append(make_album(album_title, album_artist, album_length))
    print()

print("-= Your Playlist =-")
for album in playlist:
    print()
    print(f"Album Title: {album["title"].title()}")
    print(f"  Performed By {album["artist"].title()}")
    print(f"  Length: {album.get("length", "Not Specified")}")