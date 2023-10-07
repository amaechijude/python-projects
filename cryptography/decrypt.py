alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

message = input("Input your message: ").upper()
shif_number = int(input("Input a shift numer: "))

def decrypt(cipher_message, param1_shift_number):
    decrypt_message = ""
    for char in cipher_message:
        if char in alphabet:
            position = alphabet.index(char)
            old_position = position - param1_shift_number
            while old_position < 0:
                old_position = old_position + 26
            old_char = alphabet[old_position]
            decrypt_message += old_char
        else:
            decrypt_message += old_char
    return f"The encoded message is {decrypt_message.title()}"

ecncoded_message = decrypt(message, shif_number)
print(ecncoded_message)