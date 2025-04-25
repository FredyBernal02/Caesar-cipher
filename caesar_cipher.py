from art import logo

print(logo)

alphabet = [chr(i) for i in range(97, 123)]


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % 26
            output_text += alphabet[shifted_position]
        else:
            output_text += letter  # mantiene espacios, numeros y simbolos

    print(f"\nHere is the {encode_or_decode}d result: {output_text}")


should_continue = True
while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26  # Normaliza el shift para que esté entre 0-25

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != "yes":
        should_continue = False
        print("Goodbye")
