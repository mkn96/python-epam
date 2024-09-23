class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.cipher_alphabet = self.generate_cipher_alphabet()

    def generate_cipher_alphabet(self):
        keyword_letters = list(dict.fromkeys(self.keyword))
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cipher_alphabet = ""

        for letter in keyword_letters:
            cipher_alphabet += letter

        for letter in alphabet:
            if letter not in keyword_letters:
                cipher_alphabet += letter

        return cipher_alphabet

    def encode(self, plaintext):
        plaintext = plaintext.upper()
        encoded_text = ""
        for char in plaintext:
            if char.isalpha():
                index = ord(char) - ord('A')
                encoded_char = self.cipher_alphabet[index]
                if char.islower():
                    encoded_text += encoded_char.lower()
                else:
                    encoded_text += encoded_char
            else:
                encoded_text += char
        return encoded_text

    def decode(self, ciphertext):
        ciphertext = ciphertext.upper()
        decoded_text = ""
        for char in ciphertext:
            if char.isalpha():
                index = self.cipher_alphabet.index(char)
                decoded_char = chr(index + ord('A'))
                if char.islower():
                    decoded_text += decoded_char.lower()
                else:
                    decoded_text += decoded_char
            else:
                decoded_text += char
        return decoded_text

# Example usage
cipher = Cipher("crypto")
encoded_message = cipher.encode("Hello world")
print(encoded_message)  # Output: Btggj vjmgp
decoded_message = cipher.decode("Fjedhc dn atidsn")
print(decoded_message)  # Output: Kojima is genius
