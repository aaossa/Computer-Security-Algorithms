from hashlib import md5

# Affine Cipher
# https://id0-rsa.pub/problem/5/

# Resources
# https://en.wikipedia.org/wiki/Affine_cipher

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
CIPHERTEXT_FILE = "ciphertext"


def generate_alphabet():
    alpha = {}
    for i in range(len(ALPHABET)):
        alpha[ALPHABET[i]] = i
    return alpha


def string_to_md5(string):
    return md5(string.encode('utf-8')).hexdigest()


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


class AffineCipher():

    def __init__(self, a, b, alphabet):
        self.a = a
        self.b = b
        self.alphabet = alphabet
        self.m = len(alphabet)

    def encrypt(self, x):
        return (self.a * x + self.b) % self.m

    def decrypt(self, x):
        a_1 = self.__modinv(self.a, self.m)
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

if __name__ == '__main__':
    alphabet = generate_alphabet()

    with open(CIPHERTEXT_FILE, 'r') as f:
        ciphertext = f.readline()

    a = 2
    b = 3

    Aff_cip = AffineCipher(a, b, alphabet)

    plaintext = ''
    for letter in ciphertext:
        plaintext = plaintext + ALPHABET[Aff_cip.decrypt(alphabet[letter])]

    print(plaintext)
    print()
    print(string_to_md5(plaintext))
