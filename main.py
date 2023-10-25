import encoder
import decoder
while True:
    menu = print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    menu_choice = input("Please enter an option: ")
    if menu_choice == "1":
        p_word = input("Please enter your password to encode: ")
        encoded_p = encoder.encode(p_word)
        print("Your password has been encoded and stored!")
    if menu_choice == "2":
        decoded_p = decoder.decoder(encoded_p)
        print(f"The encoded password is {encoded_p}, and the original password is {p_word}.")
    if menu_choice == "3":
        quit()