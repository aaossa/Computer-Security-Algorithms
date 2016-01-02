from base64 import b64encode
from hashlib import sha256

# Salt Alone Won't Save You
# https://id0-rsa.pub/problem/25/

# Resources
#

RECOVERED_PASSWORDS = "recovered.password"
ROCKYOU_PASSWORDS = "rockyou.txt"


def base64(hash_val):
    return b64encode(hash_val).decode('utf-8')


def hash(salt, password):
    assert(type(salt) == bytes)
    assert(type(password) == bytes)
    hash_val = sha256(password + salt).digest()
    salt = salt.decode('utf-8')
    return '$' + salt + '$' + base64(hash_val)

if __name__ == '__main__':

    test = hash(b'F&XUtH6krgmy', b'jo353ph')
    assert(test == '$F&XUtH6krgmy$jZ83Epqxk7QUo7D6Rev2AEfQuvMHokwm/QBQDfR+r6Q=')
    test = hash(b'_)lOt8&:j5%' + b'f', b'asiomas')
    assert(test == '$_)lOt8&:j5%f$Gu99fWD+K8lsHE+0lizszH8Kkb5QPrjz3osT4/LFexo=')

    PASSWORDS = []

    recovered_passwords = {}
    for recovered_p in open(RECOVERED_PASSWORDS):
        recovered_p = recovered_p.strip()
        salt = bytes(recovered_p.split('$')[1], 'utf-8')
        recovered_passwords[salt] = recovered_p

    i = 0

    for password in open(ROCKYOU_PASSWORDS, 'rb'):
        for salt, recovered_p in recovered_passwords.items():

            hash_password = hash(salt, password[:-1])

            if hash_password.strip() == recovered_p.strip():
                print(password)
                PASSWORDS.append(password)

        if not i % 15000:
            print(i, password[:-1])

        i += 1

    PASSWORDS = sorted(map(lambda x: x.strip().decode('utf-8'), PASSWORDS))
    PASSWORDS = ''.join(PASSWORDS)

    print(PASSWORDS)
