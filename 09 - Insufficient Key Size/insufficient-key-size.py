from requests import get
from subprocess import PIPE, Popen

# Insufficient Key Size
# https://id0-rsa.pub/problem/9/

# Resources
#

BASE_URL = "http://www.factordb.com/index.php?query="

PUBLIC_KEY = "publickey.rsa"
PUBLIC_KEY_PARAMETERS = "publickey.params"


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def factorize_modulus(n, online=True):
    output = {}
    if online:
        try:
            params = get(BASE_URL + str(n))
            params = params.content.decode('utf-8')
            params = params.split("index.php?id")
            clean_params = []
            for i in params:
                if i[0] == "=":
                    clean_params.append(i[1:i.find('"')])
            output["N"] = int(n)
            output["p"] = int(clean_params[1])
            output["q"] = int(clean_params[2])
        except:
            print("Offline mode")
    return output


def gen_rsa_values(filename=PUBLIC_KEY):
    p = Popen(['openssl', 'rsa', '-RSAPublicKey_in', '-text', '<', filename, '>', PUBLIC_KEY_PARAMETERS],
              stdout=PIPE, stderr=PIPE, shell=True)
    return p.communicate()


def get_rsa_values(filename=PUBLIC_KEY_PARAMETERS):
    content = {}
    with open(filename, 'r') as f:
        text = f.readlines()
        for line in text:
            if line.startswith('-----'):
                break
            elif not line.startswith('    '):
                line = line.replace(' ', '').replace('\n', '')
                line = line.split(':')
                key = line[0]
                value = line[1]
                if key == 'Exponent':
                    value = value.split('(')[0]
                content[key] = value
            elif line.startswith('    '):
                content[
                    key] += line.replace('    ', '').replace('\n', '').replace(':', '')
    return content


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

    gen_rsa_values()
    params = get_rsa_values()

    N = int(params['Modulus'], 16)
    factors = factorize_modulus(N)
    assert(factors["N"] == factors["p"] * factors["q"])

    phi = (factors["p"] - 1) * (factors["q"] - 1)
    e = int(params["Exponent"])
    factors["d"] = modinv(e, phi)

    print("d: {}".format(hex(factors["d"])))
