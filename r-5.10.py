"""
R-5.10 The constructor for the CaesarCipher class in Code Fragment 5.11 can
be implemented with a two-line body by building the forward and backward strings using
a combination of the join method and an appropriate
comprehension syntax. Give such an implementation
"""

class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""


    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        NUM_OF_LETTERS = 26
        self.forward = ''.join(chr((k + shift) % NUM_OF_LETTERS + ord( 'A' )) for k in range(NUM_OF_LETTERS))
        self.backward = ''.join(chr((k - shift) % NUM_OF_LETTERS + ord( 'A' )) for k in range(NUM_OF_LETTERS))

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
    message = "BEER AT JOE'S EAGLES ARE PLAYING"

    coded = cipher.encrypt(message)
    print('Secret:' , coded)
    assert coded != message

    answer = cipher.decrypt(coded)
    print('Message:' , answer)
    assert answer == message
