from binascii import hexlify as hex
from hashlib import sha256 as sha256hash

# Rainbow Table Hash Chain
# https://id0-rsa.pub/problem/16/

# Resources
#

HASH_CHAIN = ("bambino", "hunter42")
PASSWORD_HASH = "27ce84a6075b583086d9fc0c856f1da5d9a853507faffd7d70833c1b7accb156"


def get_line_from_file(num_line, filename='rockyou.txt'):
    index = 0
    for line in open(filename, 'rb'):
        if index == num_line:
            return line[:-1]
        index += 1
    return None


def line_count(filename='rockyou.txt'):
    lines = 0
    for line in open(filename, 'rb'):
        lines += 1
    return lines


def password_hash(pw):
    val = "".encode('utf-8')
    pw = pw.encode('utf-8')
    for _ in range(50000):
        val = sha256hash(val + pw).digest()
    return hex(val).decode('utf-8')


def reverse(password_hash, column_number):
    num_val = int(password_hash, 16)
    line_number = (num_val + column_number) % line_count()
    password = get_line_from_file(line_number).decode()
    return password


if __name__ == '__main__':

    # Test vector
    # Generating a hash chain starting from 'loveu2'

    pw = "loveu2"
    pw_hash = "c664f66b0f9cf5a777280bc0019a98d7e3b96aa894ec83d5c2d9aa14170fdda6"

    # password_hash
    assert(password_hash(pw) == pw_hash)
    # get_line_from_file
    assert(get_line_from_file(14344108) == b' \x93R3CKL3$$\x94')
    # reverse
    assert(reverse(pw_hash, column_number=0) == 'zine73')

    pw = "zine73"
    pw_hash = "c7ce2a8c0ab1ac71ef9adeb6310aca5a655e5082bf95770dcb71417a35d2ed8f"

    # "second floor"
    assert(reverse(pw_hash, column_number=1) == 'blueraccoon')

    # Real program
    pw = HASH_CHAIN[0]
    pw_hash = password_hash(pw)
    for i in range(200):
        print(pw_hash, '\t', i + 1, pw)
        pw = reverse(pw_hash, column_number=i + 1)
        pw_hash = password_hash(pw)
        if pw_hash == PASSWORD_HASH:
            print("This is the solution: {}".format(pw))
