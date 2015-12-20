from subprocess import PIPE, Popen

# Hello OpenSSL
# https://id0-rsa.pub/problem/3/

# Resources
# https://id0-rsa.pub/forum/problem/3/
# https://id0-rsa.pub/problem/21/
# https://id0-rsa.pub/info/
# http://stackoverflow.com/questions/209513/convert-hex-string-to-int-in-python
# http://crypto.stackexchange.com/questions/6593/what-data-is-saved-in-rsa-private-key

PRIVATE_KEY = 'privatekey'
RSA_VALUES = 'rsavalues'


def gen_rsa_values():
    p = Popen(['openssl', 'rsa', '-text', '<', PRIVATE_KEY, '>', RSA_VALUES],
              stdout=PIPE, stderr=PIPE, shell=True)
    return p.communicate()


def get_rsa_values():
    content = {}
    with open(RSA_VALUES, 'r') as f:
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


def hex_to_int(hex):
    return int(hex, 16)


if __name__ == '__main__':
    gen_rsa_values()
    rsa_values = get_rsa_values()

    cipher_text = input('Insert cipher text: ')

    # Decrypt
    C = hex_to_int(cipher_text)
    d = int(rsa_values['privateExponent'].replace(
        '\n', '').replace(':', ''), 16)
    N = int(rsa_values['modulus'].replace(
        '\n', '').replace(':', ''), 16)
    m = hex(pow(C, d, N))

    print(m)
