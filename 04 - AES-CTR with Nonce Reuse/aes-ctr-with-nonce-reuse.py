from binascii import unhexlify, hexlify
from itertools import cycle

# AES-CTR with Nonce Reuse
# https://id0-rsa.pub/problem/4/

# Resources
# https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_.28CTR.29
# http://travisdazell.blogspot.cl/2012/11/many-time-pad-attack-crib-drag.html

CIPHERTEXT1 = "369f9e696bffa098d2bb383fb148bd90"
CIPHERTEXT2 = "23d7847f28e4b6cc86be386cb64ca281"


def valid_word(word):
    if len(word) <= 1:
        return False
    for char in ["\\", "{", "}", "(", ")", "=", "!", "$", "[", "]", "`", "?", "|", "*", '"', "-", "'", "~", "&", "%", "+", "/"]:
        if char in word:
            return False
    for char in "0123456789":
        if char in word:
            return False
    commas = word.count(",")
    if commas > 1:
        return False
    if commas and word[-1] != ",":
        return False
    dots = word.count(".")
    if dots > 1:
        return False
    if dots and word[-1] != ".":
        return False
    if ";" in word[:-1]:
        return False
    if ":" in word[:-1]:
        return False
    return True


def valid_phrase(phrase):
    for word in phrase.split(b" "):
        word = word.decode("utf8")
        if not valid_word(word):
            return False
    return True


def xor_str(a, b):
    # http://stackoverflow.com/a/18329405/3281097
    result = int(a, 16) ^ int(b, 16)  # convert to integers and xor them
    return '{:x}'.format(result)     # convert back to hexadecimal

if __name__ == '__main__':

    original = b"a secret message"
    s = hexlify(original)

    C1_xor_C2 = xor_str(CIPHERTEXT1, CIPHERTEXT2)
    print("Ciphertext length: {}".format(len(C1_xor_C2)))

    # " the " => "t mes"
    # "t message" => " the text"
    # "secret message" => "this is the text"

    """
    for word in open("words.txt", "r"):
        word = word.replace("\n", "").lower()
        if word.endswith("t") and len(word) < 8:
            word = bytes(" " + word + " message", "utf8")
            s = hexlify(word)
            _ = 32 - len(s)

            sub_c1c2 = C1_xor_C2[_: _ + len(s)]
            dec = unhexlify(xor_str(s, sub_c1c2))
            if b" the text" in dec and valid_phrase(dec):
                print("({}, {}) {} => {}".format(_, _ + len(s), word, dec))
    """

    _ = len(CIPHERTEXT1) - len(s)
    sub_c1c2 = C1_xor_C2[_: _ + len(s)]
    dec = unhexlify(xor_str(s, sub_c1c2))
    print("({}, {}) {} => {}".format(_, _ + len(s), original, dec))
