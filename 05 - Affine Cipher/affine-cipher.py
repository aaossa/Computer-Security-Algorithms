from hashlib import md5

# Affine Cipher
# https://id0-rsa.pub/problem/5/

# Resources
# https://en.wikipedia.org/wiki/Affine_cipher

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
CIPHERTEXT_FILE = "ciphertext"


def string_to_md5(string):
    return md5(string.encode('utf-8')).hexdigest()


class AffineCipher():

    def __init__(self, a, b, alphabet):
        self.a = a
        self.b = b
        self.alphabet = self.__generate_alphabet(alphabet)
        self.m = len(alphabet)

    def encrypt(self, x):
        return (self.a * x + self.b) % self.m

    def decrypt(self, x):
        a_1 = self.__modinv(self.a, self.m)
        if type(x) == int:
            pass
        elif type(x) == str:
            x = self.alphabet[x]
        return a_1 * (x - self.b) % self.m

    def __egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.__egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def __modinv(self, a, m):
        g, x, y = self.__egcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    def __generate_alphabet(self, alphabet):
        alpha = {}
        for i in range(len(alphabet)):
            alpha[ALPHABET[i]] = i
        return alpha

if __name__ == '__main__':

    with open(CIPHERTEXT_FILE, 'r') as f:
        ciphertext = f.readline()

    a = 2
    b = 3

    Aff_cip = AffineCipher(a, b, ALPHABET)

    plaintext = ''
    for letter in ciphertext:
        plaintext = plaintext + ALPHABET[Aff_cip.decrypt(letter)]

    print(plaintext)
    print()
    print(string_to_md5(plaintext))
