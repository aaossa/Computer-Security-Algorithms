from fractions import gcd
from subprocess import PIPE, Popen

# Ps and Qs
# https://id0-rsa.pub/problem/8/

# Resources
# https://factorable.net/weakkeys12.extended.pdf
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
# http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

PUBLIC_KEYS = {'publickey_1': 'rsavalues_1',
               'publickey_2': 'rsavalues_2'}


def gen_rsa_values(inputfile, outputfile):
    p = Popen(['openssl', 'rsa', '-pubin', '-text', '-noout', '<', inputfile, '>', outputfile],
              stdout=PIPE, stderr=PIPE, shell=True)
    return p.communicate()


def get_rsa_values(rsavalues_file):
    content = {}
    with open(rsavalues_file, 'r') as f:
        text = f.readlines()
        for line in text:
            if line.startswith('-----'):
                break
            elif not line.startswith('    '):
                line = line.split(':')
                key = line[0]
                value = line[1]
                content[key] = value
            elif line.startswith('    '):
                content[key] += line.replace('    ', '')
    return content


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

if __name__ == '__main__':
    data = []
    with open('message', 'r') as f:
        c = int(f.readline(), 16)
    for k, v in PUBLIC_KEYS.items():
        gen_rsa_values(k, v)
        data.append(get_rsa_values(v))

    e = int(data[0]['Exponent'].split(' ')[1])

    n_1 = int(data[0]['Modulus'].replace(
        '\n', '').replace(':', ''), 16)
    n_2 = int(data[1]['Modulus'].replace(
        '\n', '').replace(':', ''), 16)

    p = gcd(n_1, n_2)
    q_1 = int(n_1 // p)
    phi_n1 = (p - 1) * (q_1 - 1)
    d_1 = modinv(e, phi_n1)
    m = pow(c, d_1, n_1)
    print(hex(m))
