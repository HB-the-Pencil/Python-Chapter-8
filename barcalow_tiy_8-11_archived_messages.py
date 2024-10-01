def send_messages(unsent_messages: list, sent_messages: list):
    """
    Send a list of messages one at a time.

    :param unsent_messages: List of messages that haven't been sent yet.
    :param sent_messages: List of messages that have been sent.

    :return: Prints each message with a signature (just user for now).
    """
    while unsent_messages:
        # Pop 0 so that the messages send in order.
        current = unsent_messages.pop(0)

        # Don't show the message until it's sent (for security, of course).
        print("Sending message...")
        print(f"User: {current}\n")
        sent_messages.append(current)


text_messages = ["hey", "how are you?", "im good thx",
                 "whatcha doin after school today?", "oh ok", "gtg bye"]
received_texts = []

# Print the messages, but only a copy of the unsent messages.
send_messages(text_messages[:], received_texts)

# Prove that everything was copied correctly.
print(text_messages)
print(received_texts)