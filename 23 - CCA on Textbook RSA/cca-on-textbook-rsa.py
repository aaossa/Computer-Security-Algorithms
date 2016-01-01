from requests import Session
from subprocess import PIPE, Popen

# CCA on Textbook RSA
# https://id0-rsa.pub/problem/23/

# Resources
#

BASE_URL = "https://id0-rsa.pub/problem/rsa_oracle/"

CIPHERTEXT_PATH = "ciphertext"
SERVER_PUBLIC_KEY = "publickey"
SERVER_PUBLIC_KEY_PARAMETERS = "publickey.params"

TEST_CIPHERTEXT_PATH = "ciphertext.test"
TEST_PLAINTEXT_PATH = "plaintext.test"


def decrypt_in_server(ciphertext):
    with Session() as S:
        print("Sending ciphertext to server...")
        decrypt = S.get(BASE_URL + ciphertext)
        print("Successful decryption")
    # print("Ciphertext decrypted: {}".format(decrypt.text))
    return decrypt.text


def gen_rsa_values(filename=SERVER_PUBLIC_KEY):
    p = Popen(['openssl', 'rsa', '-pubin', '-text', '<', filename, '>', SERVER_PUBLIC_KEY_PARAMETERS],
              stdout=PIPE, stderr=PIPE, shell=True)
    return p.communicate()


def get_rsa_values(filename=SERVER_PUBLIC_KEY_PARAMETERS):
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


if __name__ == '__main__':

    # Test vector
    with open(TEST_CIPHERTEXT_PATH) as f:
        test_ciphertext = f.readline()
    with open(TEST_PLAINTEXT_PATH) as f:
        test_plaintext = f.readline()

    gen_rsa_values()
    rsa_values = get_rsa_values()

    modulus = int(rsa_values['Modulus'], 16)
    exponent = int(rsa_values['Exponent'])

    original_ciphertext = int(test_ciphertext, 16)

    attack = pow(2, exponent, modulus)

    c_attack = original_ciphertext * attack
    c_attack = c_attack % modulus

    try:
        p_attack = decrypt_in_server(hex(c_attack)[2:])
    except:
        print("ERROR: Connection error while decripting attack ciphertext. Using value in memory")
        p_attack = "11a0edf0a3f2596ede1b7fcf69cf2aebe2978e706b0556b69fe375161c0ef746e"

    p_attack = int(p_attack, 16)
    p_attack = p_attack // 2
    p_attack = hex(p_attack)

    print(p_attack)

    assert(p_attack == test_plaintext)
