from string import ascii_uppercase

# Problem
# https://id0-rsa.pub/problem/32/

# Resources
#

CIPHERTEXT = ("ZNKIGKYGXIOVNKXOYGXKGRREURJIOVNKXCNOINOYXKGRREC"
              "KGQOSTUZYAXKNUCURJHKIGAYKOSZUURGFEZURUUQGZZNKCO"
              "QOVGMKGZZNKSUSKTZHAZOLOMAXKOZYMUZZUHKGZRKGYZROQ"
              "KLOLZEEKGXYURJUXCNGZKBKXBGPJADLIVBAYKZNUYKRGYZZ"
              "KTINGXGIZKXYGYZNKYURAZOUT")


def decaesar(ciphertext, key):
    plaintext = str()
    for character in ciphertext:
        q = (ord(character) - ord('A') + key) % 26
        plaintext += chr(q + ord('A'))
    return plaintext

if __name__ == '__main__':
    """
    for i in range(len(ascii_uppercase)):
        print(decaesar(CIPHERTEXT, i)[:10])
    """
    print(decaesar(CIPHERTEXT, 20))
