"""
R-5.9 Explain the changes that would have to be made to the program of Code
Fragment 5.11 so that it could perform the Caesar cipher for messages
that are written in an alphabet-based language other than English, such as
Greek, Russian, or Hebrew
"""

"""
Solution: I'd make new alphabet containing letters from ascii, Greek, Russian, Hebrew and put it into single
array. Then I'd replace 26 with the length of the newly formed array. `ord('A')` would be replaced with the first letter
of the new alphabet.
"""

class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""


    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        NUM_OF_LETTERS = 2048
        encoder = [None] * NUM_OF_LETTERS # temp array for encryption
        decoder = [None] * NUM_OF_LETTERS # temp array for decryption
        for k in range(NUM_OF_LETTERS):
            encoder[k] = chr((k + shift) % NUM_OF_LETTERS + ord( 'A' ))
            decoder[k] = chr((k - shift) % NUM_OF_LETTERS + ord( 'A' ))
        self.forward = ''.join(encoder) # will store as string
        self.backward = ''.join(decoder) # since fixed

    def encrypt(self, message):
        """Return string representing encripted message."""
        return self.transform(message, self. forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self.transform(secret, self. backward)

    def transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord( 'A' ) # index from 0 to 25
                msg[k] = code[j] # replace this character
        return ''.join(msg)

if __name__ == "__main__":
    cipher = CaesarCipher(3)
    message = "ДВА СУ ЛОША УБИЛА МИЛОША"

    coded = cipher.encrypt(message)
    print('Secret:' , coded)
    assert coded != message

    answer = cipher.decrypt(coded)
    print('Message:' , answer)
    assert answer == message
