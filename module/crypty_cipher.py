# hungarian charset support? whitespace and other char support?
# only english looks like this: [A-Z] -> [0-25] (but i guess it can be appended for hun)
# uppercase not supported - nice-to-have: random case switches for distraction

supported_chars = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz'  # 35 - [0-34]


def encrypt_vigenere(text, key):
    # The plaintext(P) and key(K) are added modulo 26.
    # Ei = (Pi + Ki) mod 26
    print("CALLED ENCRYPT")
    print("text: " + str(text))
    print("key: " + str(key))

    return text + key


def decrypt_vigenere(text, key):
    # Di = (Ei - Ki + 26) mod 26
    print("CALLED DECRYPT")
    print("text: " + str(text))
    print("key: " + str(key))

    return supported_chars
