from subprocess import PIPE, Popen
from os import remove as remove_file

# PGP - Pretty Good Privacy
# https://id0-rsa.pub/problem/19/

# Resources
# http://edoceo.com/cli/gpg
# http://www.spywarewarrior.com/uiuc/gpg/gpg-com-4.htm#1-1
# https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/4/html/Step_by_Step_Guide/s1-gnupg-export.html

# Each user has a key pair consisting of a public key and a private key
# with an associated email address. The public key is generally
# distributed freely, via something like a PGP Key Server, and the private
# key is stored privately and encrypted with a password. A message
# encrypted with a public key can only be decrypted by the corresponding
# private key. Messages can also be signed by a private key and anybody
# with the corresponding public key can verify the signature.


def encrypt(tofile=False):
    pubkey = input('Public key file: ')
    p = Popen(['gpg', '--import', pubkey],
              stdout=PIPE, stderr=PIPE)

    message = input('Message: ')
    with open('message', 'w') as f:
        f.write(message)

    p = Popen(['gpg', '--encrypt', 'message'],
              stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

    remove_file('message')


def decrypt(tofile=False):
    input_fn = input('Input filename: ')

    if tofile:
        output_fn = input('Output filename: ')
        p = Popen(['gpg', '--output', output_fn, '--decrypt', input_fn],
                  stdout=PIPE, stderr=PIPE)
    else:
        p = Popen(['gpg', '--decrypt', input_fn],
                  stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        print(out)


if __name__ == '__main__':
    p = Popen(['gpg', '--version'],
              stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

    if out:
        print('GPG installed\n')
        print('(1) Encrypt')
        print('(2) Decrypt')
        print('(3) Decrypt to file')

        option = int(input())
        if option == 1:
            encrypt()
        elif option == 2:
            decrypt()
        elif option == 3:
            decrypt(tofile=True)
    else:
        print('GPG is not installed')
        print(err)
