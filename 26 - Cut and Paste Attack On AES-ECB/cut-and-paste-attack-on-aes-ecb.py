from binascii import hexlify, unhexlify

# Cut and Paste Attack On AES-ECB
# https://id0-rsa.pub/problem/26/

# Resources
#

M1 = "Deposit amount: 5 dollars"
C1 = "0x5797791557579e322e619f12b0ccdee8802015ee0467c419e7a38bd0a254da54"
M2 = "One million dolls is quite the collection"
C2 = "0xb1e952572d6b8e00b626be86552376e2d529a1b9cafaeb3ba7533d2699636323e7e433c10a9dcdab2ed4bee54da684ca"
M3 = "Hey nice binoculars"
C3 = "0x35d0c02036354fdf6082285e0f7bd6d2fdf526bd557b045bce65a3b3e300b55e"

BLOCK_SIZE = 16


def get_blocks(message, ciphertext):
    while len(message) % BLOCK_SIZE:
        message += "_"
    message = [message[i:i + BLOCK_SIZE]
               for i in range(0, len(message), BLOCK_SIZE)]
    ciphertext = ciphertext[2:]
    ciphertext = [ciphertext[i:i + 2 * BLOCK_SIZE]
                  for i in range(0, len(ciphertext), 2 * BLOCK_SIZE)]
    return message, ciphertext


if __name__ == '__main__':

    m1, c1 = get_blocks(M1, C1)
    m2, c2 = get_blocks(M2, C2)
    m3, c3 = get_blocks(M3, C3)

    print("Message: {}".format(m1[0] + m2[0] + m3[1]))
    print("Ciphertext: 0x{}".format(c1[0] + c2[0] + c3[1]))
