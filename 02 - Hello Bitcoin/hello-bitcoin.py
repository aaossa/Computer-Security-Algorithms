from subprocess import PIPE, Popen

# Hello Bitcoin
# https://id0-rsa.pub/problem/2/

# Resources
# https://github.com/richardkiss/pycoin/blob/master/COMMAND-LINE-TOOLS.md
# https://id0-rsa.pub/forum/problem/2/solution/


def uncompressed_adress_from_secret_key(bitcoin_secret_key):
    p = Popen(['ku', '-a', '-u', bitcoin_secret_key],
              stdout=PIPE, stderr=PIPE)
    return p.communicate()


if __name__ == '__main__':
    bitcoin_secret_key = input('Bitcoin secret key: ')
    out, err = uncompressed_adress_from_secret_key(bitcoin_secret_key)
    if out != b'':
        print(out)
    else:
        print(err)
