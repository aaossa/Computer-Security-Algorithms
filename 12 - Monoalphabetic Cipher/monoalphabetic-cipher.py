from hashlib import md5

# Monoalphabetic Cipher
# https://id0-rsa.pub/problem/12/

# Resources
# http://www.ti89.com/cryptotut/mono_crack.htm

CIPHERTEXT_PATH = "ciphertext"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class MonoalphabeticCipher():

    def __init__(self, key, alphabet=UPPERCASE_LETTERS):
        assert(len(key) == len(alphabet))
        self.alphabet = alphabet
        self.key = key
        self.__generate_replaces()

    def __generate_replaces(self):
        self.__replaces_decrypt = {}
        self.__replaces_encrypt = {}
        for c, p in zip(self.key, self.alphabet):
            self.__replaces_decrypt[c] = p
            self.__replaces_encrypt[p] = c

    def decrypt(self, ciphertext):
        plaintext = ""
        for cipher_letter in ciphertext:
            plaintext += self.__replaces_decrypt[cipher_letter]
        return plaintext

    def encrypt(self, plaintext):
        ciphertext = ""
        for plain_letter in plaintext:
            ciphertext += self.__replaces_encrypt[plain_letter]
        return ciphertext


if __name__ == '__main__':

    # Test vector
    key = "UHMZGIJRSNWDPBFLQAVOCETYKX"
    cipher_text = "RGDDFTFADZ"
    plain_text = "HELLOWORLD"
    md5_hash = "e81e26d88d62aba9ab55b632f25f117d"

    MC = MonoalphabeticCipher(key)
    assert(MC.decrypt(cipher_text) == plain_text)
    assert(MC.encrypt(plain_text) == cipher_text)
    assert(md5(plain_text.encode('utf-8')).hexdigest() == md5_hash)

    # Real program
    with open(CIPHERTEXT_PATH) as f:
        cipher_text = f.readline()

    assert('cipher_text' in vars())

    MC = MonoalphabeticCipher(key="FWIUNYXZS.RGTODMQJLECKAPHB")
    message = MC.decrypt(cipher_text)
    print("Plain text: {}".format(message))

    with open("plaintext", "+w") as f:
        f.write(message)

    print("md5: {}".format(md5(message.encode('utf-8')).hexdigest()))

    """
    ##### Functions used to find the key

    # Finding E
    max_times = ("", 0)
    for letter in UPPERCASE_LETTERS:
        letter_times = cipher_text.count(letter)
        if letter_times > max_times[1]:
            max_times = (letter, letter_times)
    cipher_E = max_times[0]
    print("Cipher E: {} ({} times)".format(*max_times))



    # Finding "THE"
    candidates_the = {}
    for index in range(len(cipher_text) - 2):
        candidate_the = cipher_text[index:index + 3]
        if candidate_the.endswith(cipher_E):
            if candidate_the not in candidates_the:
                candidates_the[candidate_the] = 0
            candidates_the[candidate_the] += 1
    # http://stackoverflow.com/a/280156/3281097
    candidate_the = max(candidates_the, key=candidates_the.get)
    cipher_T = candidate_the[0]
    cipher_H = candidate_the[1]
    print("Candidate THE: {} ({} times)".format(
        candidate_the, candidates_the[candidate_the]))



    # Looking for more words

    for word in open("words.txt"):
        word = word.replace("\n", "").lower()
        if len(word) > 4 and len(word) < len("TxExTxx"):
            if word[0] == "t" and \
                    word[1] not in "the" and \
                    word[2] == "e" and \
                    word[3] not in "the" and \
                    word[4] == "t" and \
                    word[1] != word[3]:
                sub = word[4:]
                cumple = True
                for s in sub:
                    if s in candidate_the:
                        cumple = False
                if cumple:
                    print(word[1], word[3], word)

    for word in open("words.txt"):
        word = word.lower().replace("\n", "")
        if word.startswith("ye"):
            sub = word[2:]
            cumple = True
            for s in sub:
                if s in "thewny":
                    cumple = False
            if cumple:
                print(word)

    for word in open("words.txt"):
        word = word.replace("\n", "").lower()
        if len(word) == 3:
            if "aw" in word and word[1] == "a" and word[2] == "w":
                pass  # print(word)
    


    # Manual decription (looking for more words)
    partial_message = ""
    for letter in cipher_text:
        if letter == cipher_T:
            partial_message += "T"
        elif letter == cipher_H:
            partial_message += "H"
        elif letter == cipher_E:
            partial_message += "E"
        elif letter == "A":
            partial_message += "W"
        elif letter == "O":
            partial_message += "N"
        elif letter == "H":
            partial_message += "Y"
        elif letter == "F":
            partial_message += "A"
        elif letter == "J":
            partial_message += "R"
        elif letter == "L":
            partial_message += "S"
        elif letter == "S":
            partial_message += "I"
        elif letter == "T":
            partial_message += "M"
        elif letter == "X":
            partial_message += "G"
        elif letter == "B":
            partial_message += "Z"
        elif letter == "D":
            partial_message += "O"
        elif letter == "K":
            partial_message += "V"
        elif letter == "G":
            partial_message += "L"
        elif letter == "I":
            partial_message += "C"
        elif letter == "C":
            partial_message += "U"
        elif letter == "Y":
            partial_message += "F"
        elif letter == "U":
            partial_message += "D"
        elif letter == "Q":
            partial_message += "Q"
        elif letter == "M":
            partial_message += "P"
        elif letter == "P":
            partial_message += "X"
        elif letter == "W":
            partial_message += "B"
        elif letter == "R":
            partial_message += "K"
        else:
            partial_message += "."
    print(partial_message)
    """
