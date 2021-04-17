# you can play around with the order and composition of the chars
# to slightly improve complexity
supported_chars = 'aAáÁbBcCdDeEéÉfFgGhHiIíÍjJkKlLmMnNoOóÓöÖőŐpPqQrRsStTuU' + \
                    'úÚüÜűŰvVwWxXyYzZ ,.!?#@[]&'


class Vigenere:
    def __init__(self, text, key):
        self.text = text.strip()
        self.key = key.strip()
        self.char_len = len(supported_chars)
        self.text_len = len(self.text)
        self.key_len = len(self.key)

    def crypt(self, func):
        crypted_text = ''
        for index in range(self.text_len):
            t_supp_index = supported_chars.find(self.text[index])
            k_supp_index = supported_chars.find(self.key[index % self.key_len])

            en_ch_i = func(t_supp_index, k_supp_index) % self.char_len
            crypted_text += supported_chars[en_ch_i]

        return crypted_text

    def encrypt(self):
        return self.crypt(lambda t_i, k_i: (t_i + k_i))

    def decrypt(self):
        return self.crypt(lambda t_i, k_i: (t_i - k_i))
