from utils import letter_to_index, index_to_letter


def c_encrypt(message, k):
    encrypted = ''
    message_length = len(message)

    for i in range(message_length):
        letter = message[i]
        index = letter_to_index(letter)

        if index == -1:
            encrypted += letter
            continue

        new_index = (index + k) % 26
        new_letter = index_to_letter(new_index)

        encrypted += new_letter

    return encrypted