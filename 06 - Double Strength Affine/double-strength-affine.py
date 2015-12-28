from hashlib import md5
from gc import collect
from time import time

# Double Strength Affine
# https://id0-rsa.pub/problem/6/

# Resources
#

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
CIPHERTEXT_FILE = "ciphertext"


def string_to_md5(string):
    return md5(string.encode('utf-8')).hexdigest()


class DoubleStrengthAffineCipher():

    def __init__(self, a, b, alphabet):
        self.a = a
        self.b = b
        self.blocks = []
        self.alphabet = self.__generate_alphabet(alphabet)
        self.m = len(self.alphabet)

    def __egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.__egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def __generate_alphabet(self, alphabet):
        alpha = {}
        for i in range(len(alphabet)):
            for j in range(len(alphabet)):
                block = alphabet[i] + alphabet[j]
                self.blocks.append(block)
                alpha[block] = 29 * i + j
        return alpha

    def __modinv(self, a, m):
        g, x, y = self.__egcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    def encrypt(self, x):
        return (self.a * x + self.b) % self.m

    def decrypt(self, x):
        a_1 = self.__modinv(self.a, self.m)
        if type(x) == int:
            pass
        elif type(x) == str:
            x = self.alphabet[x]
        return a_1 * (x - self.b) % self.m


def valid_word(word):
    commas = word.count(',')
    dots = word.count('.')
    if len(word) == 0:
        return False
    if word[0] in ['.', ',']:
        return False
    if commas > 1:
        return False
    if commas == 1 and word[-1] != ',':
        return False
    """
    if dots > 1:
        return False
    """
    if dots == 1 and word[-1] != '.':
        return False
    if len(word) < 1:
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

    # No puede calcular con multiplos de 29

    for a in range(1, pow(len(ALPHABET), 2)):
        if (a % 29 != 0):

            start = time()

            for b in range(0, pow(len(ALPHABET), 2)):

                DSA_cip = DoubleStrengthAffineCipher(a, b, ALPHABET)

                plaintext = ''
                for i in range(0, len(ciphertext), 2):
                    block = ciphertext[i] + ciphertext[i + 1]
                    plaintext = plaintext + \
                        DSA_cip.blocks[DSA_cip.decrypt(block)]

                plaintext_words = iter(plaintext.lower().split(' '))
                count = 0

                plaintext_word = next(plaintext_words)
                while valid_word(plaintext_word):
                    for word in dictionary[plaintext_word[0]]:
                        word = word.replace('\n', '')
                        if plaintext_word == word:
                            count += 1
                            if len(word) > 3:
                                print(
                                    "Palabra candidata ({}, {}): {}".format(a, b, word))
                        if word > plaintext_word:
                            break
                    collect()
                    try:
                        plaintext_word = next(plaintext_words)
                    except:
                        print(plaintext_word)
                        break

                if count > 10:
                    print("({}, {}) => {}".format(a, b, count))
                if count > maxcount and plaintext_word == None:
                    maxcount = count
                    maxtuple = (a, b)
                    print("({}, {}) -> #words = {}".format(a, b, maxcount))
                    print(plaintext)
                    print()

                collect()

            end = time()

            print(a, end - start)

            collect()

        else:
            maxcount = 0
            maxtuple = tuple()
            print("=============================")

    collect()

    # DSA_cip = DoubleStrengthAffineCipher(maxtuple[0], maxtuple[1], ALPHABET)
    DSA_cip = DoubleStrengthAffineCipher(543, 207, ALPHABET)

    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        block = ciphertext[i] + ciphertext[i + 1]
        plaintext = plaintext + DSA_cip.blocks[DSA_cip.decrypt(block)]

    print(plaintext)
    print()
    print('MD5 hash: {}'.format(string_to_md5(plaintext)))
