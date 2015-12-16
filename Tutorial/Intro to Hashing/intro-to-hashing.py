from hashlib import md5, sha256

# Hashing
# https://id0-rsa.pub/problem/18/

# Resources
# https://en.wikipedia.org/wiki/Hash_function
# https://en.wikipedia.org/wiki/List_of_hash_functions

# A hash function is one which takes any amount of input and gives a fixed
# size output. Hash functions have many uses in computing, but here we're
# going to focus on cryptographic hash functions. In addition to giving a
# fixed size output for any input, cryptographic hash functions have a
# couple other important qualities. One is that they're difficult to
# reverse. That means that given the output of a hash function, it's hard
# to figure out an input to the hash function that would result in that
# output. Another is that they're collision resistant, which means that
# it's hard to find two inputs to the hash function that result in the
# same output.


class Hashing:

    @staticmethod
    def string_to_md5(string):
        return md5(string.encode('utf-8')).hexdigest()

    @staticmethod
    def string_to_sha256(string):
        return sha256(string.encode('utf-8')).hexdigest()


if __name__ == '__main__':

    print('(1) String to md5')
    print('(2) String to sha256')
    print('(3) String to md5 to sha256')
    print('(4) String to sha256 to md5')

    option = int(input())
    string = input('String: ')
    if option == 1:
        print(Hashing.string_to_md5(string))
    elif option == 2:
        print(Hashing.string_to_sha256(string))
    elif option == 3:
        print(Hashing.string_to_sha256(Hashing.string_to_md5(string)))
    elif option == 4:
        print(Hashing.string_to_md5(Hashing.string_to_sha256(string)))
