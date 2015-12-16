from auxiliar import prime
from fractions import gcd
from random import choice, randint

# RSA
# https://id0-rsa.pub/problem/21/

# Resources
# http://www.rhyous.com/2011/10/27/the-step-by-step-rsa-algorithm/

# The basic idea behind public key cryptography is that there are two
# keys, a public key and a private key. The public key is used for
# encrypting and verifying messages and can be distributed to anyone
# whereas the private key is used for decrypting and signing messages and
# should be kept secret by the party that generated the keys.


class RSA:

    MIN = 10
    MAX = 100

    @staticmethod
    def KeyGeneration():
        p = RSA.__pickup_random_prime()
        q = RSA.__pickup_random_prime()
        N = p * q
        phi = (p - 1) * (q - 1)
        e = RSA.__pickup_e(phi)
        d = RSA.__pickup_d(e, phi)
        return (e, N), d

    @staticmethod
    def Encryption(m, public_key):
        e, N = public_key
        c = (m ** e) % N
        return c

    @staticmethod
    def Decryption(c, public_key, private_key):
        e, N = public_key
        d = private_key
        m = (c ** d) % N
        return m

    def __pickup_random_prime():
        primes = prime()
        top_limit = randint(RSA.MIN, RSA.MAX)
        for _ in range(RSA.MIN, top_limit):
            next(primes)
        return next(primes)

    def __pickup_e(phi):
        e = 3
        e_candidates = []
        while e < phi:
            if gcd(e, phi) == 1:
                e_candidates.append(e)
            e += 2
        return choice(e_candidates)

    def __pickup_d(e, phi):
        for d in range(3, phi):
            if d * e % phi == 1 and e % 2 == 1:
                return d


def demo():
    public_key = (
        0x3, 0x64ac4671cb4401e906cd273a2ecbc679f55b879f0ecb25eefcb377ac724ee3b1)
    private_key = 0x431d844bdcd801460488c4d17487d9a5ccc95698301d6ab2e218e4b575d52ea3
    c = 0x599f55a1b0520a19233c169b8c339f10695f9e61c92bd8fd3c17c8bba0d5677e

    return RSA.Decryption(c, public_key, private_key)


if __name__ == '__main__':
    public_key, private_key = RSA.KeyGeneration()
    print('Public key: {}'.format(public_key))
    print('Private key: {}'.format(private_key))

    m = 100
    c = RSA.Encryption(100, public_key)
    print('m = {} encrypted is {}'.format(m, c))

    m = RSA.Decryption(c, public_key, private_key)
    print('c = {} decrypted is {}'.format(c, m))
