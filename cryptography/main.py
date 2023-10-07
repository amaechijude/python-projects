alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

message = input("Input your message: ").upper()
shif_number = int(input("Input a shift numer: "))

def encrypt(param_message, param_shift_number):
    cipher_message = ""
    for char in param_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + param_shift_number
            while new_position > 25:
                new_position = new_position - 26
            new_char = alphabet[new_position]
            cipher_message += new_char
        else:
            cipher_message += char
    return f"The encoded message is {cipher_message}"

ecncoded_message = encrypt(message, shif_number)
print(ecncoded_message)