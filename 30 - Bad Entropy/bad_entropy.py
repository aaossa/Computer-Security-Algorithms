from binascii import unhexlify
from datetime import datetime
from hashlib import md5
from time import mktime
from Crypto.Cipher import AES

# Problem
# https://id0-rsa.pub/problem/30/

# Resources
#


def genkey(timestamp):
    i = str(timestamp).encode("ascii")
    return md5(i).digest()


def trykey(secret):
    ciphertext = unhexlify(b"a99210d796a1e37503febf65c329c1b2")
    cipher = AES.AESCipher(secret, AES.MODE_ECB)
    decripted = cipher.decrypt(ciphertext)
    return decripted.decode("ascii")

if __name__ == '__main__':

    starts_at = datetime(2016, 1, 25, 0, 0)
    timestamp = int(mktime(starts_at.timetuple()))
    end = timestamp + 7 * 24 * 60 * 60

    while timestamp <= end:
        key = genkey(timestamp)
        try:
            print(trykey(key))
        except:
            pass
        timestamp += 1
