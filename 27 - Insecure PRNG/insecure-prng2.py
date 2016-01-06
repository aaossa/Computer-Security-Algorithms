from binascii import unhexlify
from hashlib import sha256

# Insecure PRNG
# https://id0-rsa.pub/problem/27/

# Resources
#

BASE58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def bsd_rand(seed):
    def rand():
        nonlocal seed
        seed = (1103515245 * seed + 12345) & 0x7fffffff
        return seed
    return rand


def base_encode(number, base=58, alphabet=BASE58):
    # https://gist.github.com/ianoxley/865912

    encode = ''

    if (number < 0):
        return ''

    while (number >= base):
        mod = number % base
        encode = alphabet[mod] + encode
        number = number // base

    if (number):
        encode = alphabet[number] + encode

    return encode


def decode_base58(bc, length):
    # https://github.com/ConceptPending/PythonBTCTools/blob/master/btctools.py
    n = 0
    for char in bc:
        n = n * 58 + BASE58.index(char)
    return n


def key_to_wif(string):
    # https://en.bitcoin.it/wiki/Wallet_import_format
    # https://github.com/ConceptPending/PythonBTCTools/blob/master/btctools.py
    step1 = string.zfill(64)
    step2 = '80' + step1
    step3 = sha256(unhexlify(step2)).hexdigest()
    step4 = sha256(unhexlify(step3)).hexdigest()
    step5 = step4[:8]  # checksum
    step6 = step2 + step5
    step7 = ''.join([BASE58[int(step6, 16) // (58**l) % 58]
                     for l in range(len(step6))])[::-1].lstrip('1')
    return step7


def wif_to_key(string):
    step1 = string
    step2 = hex(decode_base58(step1, len(step1)))[2:]
    step3 = step2[:-8]
    step4 = step3[2:]
    return step4


if __name__ == '__main__':

    # Test vector

    m = pow(2, 31)
    a = 1103515245
    c = 12345
    seed = 0x123

    f = bsd_rand(seed)
    key = ""
    for _ in range(256):
        N = f()
        key += str(N >> 29 & 1)

    test_key = "3a71c3dc3b5dad959973a074cff234bf09735ed305dfc6247357142a962bd3fa"
    assert("%x" % int(key, 2) == test_key)
    test_wif = "5JG2Tvy2sgek4MkDHrNbRp6HcVya6rHELaNPxX4eKJ8z6jmDLWA"
    assert(key_to_wif(test_key) == test_wif)
    assert(wif_to_key(key_to_wif(key)) == key)

    # print(int(test_key[-2], 16))
    # print(int(key[-8:-4], 2))
    # print(int(test_key, 16) == int(key, 2))
    # print(bin(int(test_key, 16))[2:] == key.lstrip('0'))

    wif = "5KQFVHAxyMMVsDz75bDp7S4NpwoQz2FgR8b7DjyEhUo6saJfS73"
    key = wif_to_key(wif)
    key_bits = bin(int(key, 16))[2:].rjust(256, '0')
    for current_seed in range(457 * 1000 * 1000, m):
        def try_seed():
            f = bsd_rand(current_seed)
            for current_bit in key_bits:
                N = f()
                if str(N >> 29 & 1) != current_bit:
                    return
            print("SEED: {}".format(current_seed))
        try_seed()
        if not current_seed % (100 * 1000):
            print(current_seed)
