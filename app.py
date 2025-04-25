import streamlit as st
from art import logo

# Mostrar el logo al inicio
st.title("Caesar Cipher")
st.text(logo)

# Función de cifrado César
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Procesar el texto con el cifrado César
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter  # Si el carácter no está en el alfabeto, se mantiene igual

    return output_text


# Interfaz de usuario en Streamlit
direction = st.radio("Choose the operation:", ('encode', 'decode'))
text = st.text_area("Enter your message:")
shift = st.slider("Shift number", 1, 25, 3)

if st.button('Apply'):
    result = caesar(text.lower(), shift, direction)
    st.write(f"Here is the {direction}d result: {result}")
