from hashlib import sha256 as hashlib_sha256

# Fast Hashing Passwords
# https://id0-rsa.pub/problem/24/

# Resources
#


def sha256(password_bytes):
    return hashlib_sha256(password_bytes).hexdigest()


if __name__ == '__main__':

    smallest_hash = ('f' * 64, None)
    largest_hash = ('0' * 64, None)

    for password in open("rockyou.txt", "rb"):
        password = password[:-1]
        hashed_password = sha256(password)
        if hashed_password < smallest_hash[0]:
            smallest_hash = (hashed_password, password)
        if hashed_password > largest_hash[0]:
            largest_hash = (hashed_password, password)

    print("Smallest hash: {} ({})".format(*smallest_hash))
    print("Largest hash: {} ({})".format(*largest_hash))

    print("Answer: {}".format(largest_hash[1] + smallest_hash[1]))
