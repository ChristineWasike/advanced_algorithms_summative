def encryption(message, key):
    # array storing rows of encrypted message
    encryption_array = [''] * key

    for index in range(len(message)):
        # adding letters from message to respective row/string
        encryption_array[index % key] += message[index]

    # stores final encrypted string
    encrypted_message = ''

    for string in encryption_array:
        # forming a single string from rows generated in encryption
        encrypted_message += string

    # final encrypted message
    return encrypted_message


def decryption(encrypted_message, key):
    break_point = int(len(encrypted_message) / key)
    decrypt = []
    decryption_array = []
    message = ''
    for index in range(len(encrypted_message) + 1):
        decrypt.append(list(encrypted_message)[index:len(list(encrypted_message)):break_point])
        decryption_array += decrypt[index]
        if len(decryption_array) == len(encrypted_message):
            break

    for index in range(len(decrypt)):
        message += (decrypt[index][0] + decrypt[index][1])

    return message


if __name__ == '__main__':
    print(encryption('plain text', 2))  # pantxli et
    print(encryption('plain text', 3))  # pittlnea x

    print(decryption('pantxli et', 2))  # plain text
    print(decryption('pittlnea x', 3))  # Check this.
