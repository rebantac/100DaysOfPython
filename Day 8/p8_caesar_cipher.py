from p8_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text_msg, shift_no, dirtn):
    caesar_text = ""

    for letter in text_msg:
        if letter in alphabet:
            letter_index = alphabet.index(letter)

            if dirtn == "encode":
                new_index = letter_index + shift_no
                new_index = new_index % 26 # starts from 'a' after 'z'
            elif dirtn == "decode":
                new_index = letter_index - shift_no

            caesar_text += alphabet[new_index]
        else:
            caesar_text += letter
    
    print(f"The {dirtn}d text is:", caesar_text)


print(logo)

flag = "yes"
while flag == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # if user enters shift number more than the number of alphabets 

    caesar(text, shift, direction)

    flag = input("Press yes to continue and no to exit: ")

print("Goodbye!")