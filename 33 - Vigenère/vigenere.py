from string import ascii_uppercase

# Problem
# https://id0-rsa.pub/problem/33/

# Resources
#

abc_to_int = {ascii_uppercase[pos]: pos for pos in range(len(ascii_uppercase))}


class Vigenere:

    L = len(ascii_uppercase)

    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        expansion, extra = divmod(len(plaintext), len(self.key))
        key = self.key * expansion + self.key[:extra]
        output = str()
        for i in range(len(plaintext)):
            c_i = (abc_to_int[plaintext[i]] + abc_to_int[key[i]]) % Vigenere.L
            output += ascii_uppercase[c_i]
        return output

    def decrypt(self, ciphertext):
        expansion, extra = divmod(len(ciphertext), len(self.key))
        key = self.key * expansion + self.key[:extra]
        output = str()
        for i in range(len(ciphertext)):
            c_i = (abc_to_int[ciphertext[i]] - abc_to_int[key[i]]) % Vigenere.L
            output += ascii_uppercase[c_i]
        return output


if __name__ == '__main__':
    # Test vector
    PT = "HELLOWORLD"
    KEY = "BC"
    CT = "IGMNPYPTMF"
    V = Vigenere(KEY)
    V.encrypt(PT)
    V.decrypt(CT)

    # Exercise
    with open("ciphertext") as f:
        ct = f.read().replace(" ", "").replace("\n", "")

    # Tomar pedazo a pedazo
    # Obtener posible key
    # Calcular texto en ingles
    # Imprimir top 10
