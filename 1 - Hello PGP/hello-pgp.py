from subprocess import PIPE, Popen

# Hello PGP
# https://id0-rsa.pub/problem/1/

# Resources
# http://stackoverflow.com/a/5898031/3281097
# https://docs.python.org/3.4/library/itertools.html#itertools.product

WORDS_PATH = 'words.txt'
MESSAGE_PATH = 'msm.txt'


def words(ignore=0):
    with open(WORDS_PATH, 'r') as f:
        line = f.readline()
        for _ in range(ignore):
            line = f.readline()
        while line:
            yield line.replace('\n', '')
            line = f.readline()


def try_passphrase(passphrase):
    p = Popen(['gpg', '--batch', '--yes', '--passphrase', passphrase, '--decrypt', MESSAGE_PATH],
              stdout=PIPE, stderr=PIPE)
    return p.communicate()


if __name__ == '__main__':

    IGNORE = 175400

    i = IGNORE
    for passphrase in words(ignore=IGNORE):
        i += 1
        out, err = try_passphrase(passphrase)
        if out != b'':
            print('Success!')
            print(out)
            print(i)
            print(passphrase)
            break
        if not i % 200:
            print(i, passphrase)

    print(out)
    print(err)
