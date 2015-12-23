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


def valid_word(word):
    commas = word.count(',')
    dots = word.count('.')
    if commas > 1:
        return False
    if commas == 1 and word[-1] != ',':
        return False
    if dots > 1:
        return False
    if dots == 1 and word[-1] != '.':
        return False
    if len(word) <= 1:
        return False
    return True


if __name__ == '__main__':

    with open(CIPHERTEXT_FILE, 'r') as f:
        ciphertext = f.readline()

    maxcount = 0
    maxtuple = tuple()

    dictionary = {}

    for word in open('words.txt'):
        word = word.lower()
        if word[0] not in dictionary:
            dictionary[word[0]] = []
        dictionary[word[0]].append(word)

    for a in range(1, len(ALPHABET)):
        for b in range(0, len(ALPHABET)):

            Aff_cip = AffineCipher(a, b, ALPHABET)

            plaintext = ''
            for letter in ciphertext:
                plaintext = plaintext + ALPHABET[Aff_cip.decrypt(letter)]

            plaintext_words = plaintext.lower().split(' ')
            count = 0

            for plaintext_word in plaintext_words:
                if valid_word(plaintext_word):
                    for word in dictionary[plaintext_word[0]]:
                        word = word.replace('\n', '')
                        if plaintext_word == word:
                            count += 1
                        if word > plaintext_word:
                            break
            if count > maxcount:
                maxcount = count
                maxtuple = (a, b)

    Aff_cip = AffineCipher(maxtuple[0], maxtuple[1], ALPHABET)

    plaintext = ''
    for letter in ciphertext:
        plaintext = plaintext + ALPHABET[Aff_cip.decrypt(letter)]

    print(plaintext)
    print()
    print('MD5 hash: {}'.format(string_to_md5(plaintext)))
