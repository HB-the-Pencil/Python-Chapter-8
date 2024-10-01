def show_messages(messages: list):
    """
    Show a list of messages that a user has sent.

    :param messages: List of messages sent.

    :return: Prints each message with a signature (just user for now).
    """
    for message in messages:
        print(f"User: {message}")


text_messages = ["hey", "how are you?", "im good thx",
                 "whatcha doin after school today?", "oh ok", "gtg bye"]

# Print the messages.
show_messages(text_messages)