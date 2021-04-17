# hungarian charset support? whitespace and other char support?
# only english looks like this: [A-Z] -> [0-25] (but i guess it can be appended for hun)
# uppercase not supported - nice-to-have: random case switches for distraction

supported_chars = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz ,.!?'  # 40 - [0-39]


def encrypt_vigenere(text, key):
    # The plaintext(P) and key(K) are added modulo 26.
    # Ei = (Pi + Ki) mod 26
    text = text.strip()
    key = key.strip()

    encrypted_text = ""
    char_len = len(supported_chars)
    text_len = len(text)
    key_len = len(key)

    for index in range(text_len):
        t_supp_index = supported_chars.find(text[index])
        k_supp_index = supported_chars.find(key[index % key_len])

        en_ch_i = (t_supp_index + k_supp_index) % char_len
        encrypted_text += supported_chars[en_ch_i]

    return encrypted_text


def decrypt_vigenere(text, key):
    # Di = (Ei - Ki + 26) mod 26
    print("CALLED DECRYPT")
    print("text: " + str(text))
    print("key: " + str(key))

    return supported_chars
