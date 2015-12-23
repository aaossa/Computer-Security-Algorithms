# Factoring RSA With CRT Optimization
# https://id0-rsa.pub/problem/15/

# Resources
# https://people.redhat.com/~fweimer/rsa-crt-leaks.pdf


class RSA_with_CRT_optim():

    @property
    def d(self):
        return self.__modinv(self.e, self.phi)

    @property
    def phi(self):
        return (self.p - 1) * (self.q - 1)

    @property
    def dp(self):
        return self.__modinv(self.e, self.p - 1)

    @property
    def dq(self):
        return self.__modinv(self.e, self.q - 1)

    @property
    def qinv(self):
        return self.__modinv(self.q, self.p)

    @property
    def y1(self):
        return pow(self.x, self.dp, self.p)

    @property
    def y2(self):
        return pow(self.c, self.dq, self.q)

    @property
    def h(self):
        # self.qinv * (self.y1 - self.y2) % self.p
        return (self.qinv * (self.y1 - self.y2)) % self.p

    @property
    def y(self):
        return self.y2 + self.h * self.q

    @property
    def private_key(self):
        return (self.p, self.q, self.dp, self.dq, self.qinv)

    def __egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.__egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def __modinv(self, a, m):
        g, x, y = self.__egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m


def gcd(a, b, upper_bound=None):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    A = RSA_with_CRT_optim()
    # RSA parameters
    A.e = int('0x10001', 16)
    A.n = int('0x90def3c2c91ae9bf6089ec8857960d567fdbcd7c2c3ea713046977231e65f44e1b91550971d4e5d43b51675fae4ba640add3af02dad4bf68c3ddef3a98907e1e01156de7a4474d9fce2ba8c055f44673c703a72a111a06f8a7b2fe582463938d802e91630e1e1b5483b1774e608eb4368c6bbf4da375319d9a2799bf8a5ae453', 16)
    # A message x was signed with these parameters
    A.message_x = int('0xdeadc0de', 16)
    # The failure happened when computing the signature y
    A.signature_y = int('0x17d7f90a4597fb2bbbb41d1a70f505f0d8c5cb53faaafea259150eb6910fb08fbf1ba40e42de70c596fb0032d132c9c6ce46c650999ad5f14a990d205984260146e2949b819dc8732beceed452701d88b2c8723b410fce739009df89930424c566af5102403981c26c3e75d9c62065a347e815b26984dcd3b5f02fc8a8092051', 16)

    # Steps:
    # Given that the computation of y1 or y2 failed, recover a factor of n
    A.p = gcd(pow(A.signature_y, A.e) - A.message_x, A.n)
    A.q = A.n // A.p

    # Recover d and submit d mod 1000000007
    # d:  e * d equiv 1 (mod phi(n))
    # phi(n) = (p - 1) * (q - 1)
    # We have e and n (n = p * q), but no p or q
    print(A.d % 1000000007)
