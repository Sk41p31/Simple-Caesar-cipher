from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(f"{logo}\n")


def caesar(text_to_change, shift_length, choice) :
    
    if choice == 'encode' :
        encoded_text = ''
        for letter in text_to_change:
            if letter in alphabet :
                pos = (alphabet.index(letter) + shift_length) % len(alphabet)
                encoded_text += alphabet[pos]
            else:
                encoded_text += letter
        print(f"Your encrypted message is: {encoded_text}\n")
        
    elif choice == 'decode' :
        decoded_text = ''
        for letter in text_to_change:
            if letter in alphabet :
                pos = alphabet.index(letter) - shift_length
                decoded_text += alphabet[pos]
            else:
                encoded_text += letter
        print(f"Your decrypted message is: {decoded_text}\n")

end = 'yes'
while end == 'yes' :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)
    end = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")




