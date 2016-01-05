from base64 import b64decode, b64decode
from binascii import hexlify, unhexlify
from requests import get

# CBC Padding Attack
# https://id0-rsa.pub/problem/22/

# Resources
# https://github.com/escbar/pypadbuster
# https://en.wikipedia.org/wiki/Padding_oracle_attack#Example_of_the_attack_on_CBC_encryption
# http://dabeaz.blogspot.cl/2010/01/few-useful-bytearray-tricks.html
# http://crypto.stackexchange.com/questions/3714/how-does-a-padding-oracle-attack-work
# http://robertheaton.com/2013/07/29/padding-oracle-attack/

CIPHERTEXT = "ciphertext"
BASE_URL = "http://id0-rsa.pub/problem/cbc_padding_oracle/"


def send_ciphertext(message):
    if type(message) == bytes:
        message = message.decode('utf-8')
    decrypt = get(BASE_URL + message)
    return decrypt.status_code, decrypt.text


def xorstring(key, data):
    build = ""
    for i in range(0, len(data)):
        build += chr(ord(key[i % len(key)]) ^ ord(data[i]))
    return build

if __name__ == '__main__':

    with open(CIPHERTEXT) as f:
        # Valid ciphertext c
        message = f.readline()

    status, decryption = send_ciphertext(message)
    assert(status == 200)
    assert(decryption == "Got it, thanks :)")
