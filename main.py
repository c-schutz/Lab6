import encoder
import decoder

p_word = input("Enter password: ")

encoded_p = encoder.encode(p_word)

decoded_p = decoder.decoder(encoded_p)

print(decoded_p)