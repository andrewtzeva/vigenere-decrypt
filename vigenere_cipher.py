from utils import letter_to_index, index_to_letter


def v_decrypt(message, key):
    decrypted = ''
    message_length = len(message)
    key_length = len(key)
    j = -1  # Index j increases if character is alphabetical

    for i in range(message_length):
        letter = message[i]
        index = letter_to_index(letter)

        if index == -1:  # Ignoring non-alphabetical characters
            decrypted += letter
            continue

        j += 1
        key_index = letter_to_index(key[j % key_length])
        new_index = (index - key_index) % 26
        new_letter = index_to_letter(new_index)

        decrypted += new_letter

    return decrypted



def v_encrypt(message, key):
    encrypted = ''
    message_length = len(message)
    key_length = len(key)
    j = -1  # Index j increases if character is alphabetical

    for i in range(message_length):
        letter = message[i]
        index = letter_to_index(letter)

        if index == -1:  # Ignoring non-alphabetical characters
            encrypted += letter
            continue

        j += 1
        key_index = letter_to_index(key[j % key_length])
        new_index = (index + key_index) % 26
        new_letter = index_to_letter(new_index)

        encrypted += new_letter

    return encrypted

