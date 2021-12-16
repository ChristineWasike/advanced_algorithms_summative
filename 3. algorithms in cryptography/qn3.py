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
    # establishing the points of creating the rows/string again
    break_point = int(len(encrypted_message) / key)
    # stores the final decrypted message as list
    decrypt = []
    # stores the deconstructed rows from the encrypted message
    decryption_array = []
    # stores the decrypted message
    message = ''

    for index in range(len(encrypted_message) + 1):
        # check for starter letters that make the first letters in the deconstructed rows
        if len(encrypted_message) % key != 0 and index < (break_point + 1):
            # append the letter from index to length of encrypted message with a breakpoint + 1 step
            decrypt.append(list(encrypted_message)[index:len(list(encrypted_message)):(break_point + 1)])

        else:
            # append the letter from index to length of encrypted message with a breakpoint step
            decrypt.append(list(encrypted_message)[index:len(list(encrypted_message)):break_point])
        print(decrypt)

        # add the letter in the decrypt array at index to decryption array
        decryption_array += decrypt[index]

        # check if length of decryption array is equal to length of message and if true break
        if len(decryption_array) == len(encrypted_message):
            break

    # construct the string
    for index in range(len(decrypt)):
        message += (decrypt[index][0] + decrypt[index][1])

    return message


if __name__ == '__main__':
    # Testing
    print(encryption('plain text', 2))  # pantxli et
    print(encryption('plain text', 3))  # pittlnea x

    print(decryption('pantxli et', 2))  # plain text
    print(decryption('pittlnea x', 3))  # Check this.
