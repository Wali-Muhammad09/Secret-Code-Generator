import streamlit as st

# Custom encoding and decoding dictionaries
custom_codes = {
    "a": "df", "b": "ew", "c": "rs", "d": "fd", "e": "zq",
    "f": "qz", "g": "iq", "h": "ze", "i": "qi", "j": "ez",
    "k": "dd", "l": "ff", "m": "cv", "n": "vc", "o": "nb",
    "p": "hg", "q": "lk", "r": "kl", "s": "ik", "t": "ki",
    "u": "sa", "v": "as", "w": "zp", "x": "pz", "y": "cw",
    "z": "wc", " ": " "
}


translated_code = {v: k for k, v in custom_codes.items()}


st.title("Secret Code Converter")

mode = st.radio("Choose mode:", ["Encode", "Decode"])

user_input = st.text_input("Enter your text:")

if user_input:
    if mode == "Encode":
        result = ""
        for char in user_input.lower():
            if char in custom_codes:
                result += custom_codes[char]
            else:
                result += char
        st.subheader("🔒 Encoded Text:")
        st.code(result)

    elif mode == "Decode":
        result = ""
        i = 0
        while i < len(user_input):

            if user_input[i] == " ":
                result += " "
                i += 1
            else:
                chunk = user_input[i:i+2]
                decoded_char = translated_code.get(chunk, '?')
                result += decoded_char
                i += 2
        st.subheader("🔓 Decoded Text:")
        st.code(result)
