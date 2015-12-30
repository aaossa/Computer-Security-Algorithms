# ECDSA Nonce Recovery
# https://id0-rsa.pub/problem/17/

# Resources
# http://eprint.iacr.org/2015/839.pdf (Seccion 2.3)

z1 = 78963682628359021178354263774457319969002651313568557216154777320971976772376
s1 = 5416854926380100427833180746305766840425542218870878667299
r1 = 5568285309948811794296918647045908208072077338037998537885
SIGNATURE1 = (s1, r1)

z2 = 62159883521253885305257821420764054581335542629545274203255594975380151338879
s2 = 1063435989394679868923901244364688588218477569545628548100
r2 = 5568285309948811794296918647045908208072077338037998537885
SIGNATURE2 = (s2, r2)

n = 6277101735386680763835789423176059013767194773182842284081


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    while a < 0:
        a += m
    g, x, y = egcd(a, m)
    if g != 1:
        print("a = {}".format(a))
        print("m = {}".format(m))
        print("g = {}".format(g))
        raise Exception('modular inverse does not exist')
    else:
        return x % m

if __name__ == '__main__':
    # You can recover k given two signature / message pairs that used the same
    # k and signing key, which can lead to the signing key being compromised
    k = (((z1 - z2) * modinv(s1 - s2, n)) % n)

    # Recover k (submit your answer in hex)    
    print("k = {}".format(k))
    print("k (hex) = {}".format(hex(k)))
