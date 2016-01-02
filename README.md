# Computer Security Algorithms

Problems related to computer security. Algorithms written in Python. [Follow the Tutorial](https://id0-rsa.pub/)

### Main topics

* **PGP:** PGP stands for [*Pretty Good Privacy*](https://en.wikipedia.org/wiki/Pretty_Good_Privacy). Is a program used to facilitate encrypt and decrypt your mail. PGP "has proven itself quite capable of resisting even the most sophisticated forms of analysis" ([PGP faqs](http://www.faqs.org/faqs/pgp-faq/part1/))

* **RSA:** RSA stands for [*Rivest-Shamir-Adleman*](https://en.wikipedia.org/wiki/RSA_(cryptosystem)). Is a widely used public-key cryptosystem "based on the practical difficulty of factoring the product of two large prime numbers" ([RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)))

* **Hashing:** A [*hash function*](https://en.wikipedia.org/wiki/Hash_function) maps data of arbitrary size to data of fixed size. An [ideal hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function) maps randomly, avoid colissions and is impossible to invert.

### Scripts

* **Hello PGP** Use PGP programatically. Recover the message encrypted with a single English word.

* **Hello Bitcoin** Do you know how bitcoin addresses are constructed?

* **Hello OpenSSL** Can you read and use an OpenSSL RSA key?

* **AES-CTR with Nonce Reuse** Can you exploit a reused nonce?

* **Affine Cipher** Can you brute force this classical cipher?

* **Double Strength Affine** A slight security upgrade, is it enought?

* **Ps and Qs** RSA keys generated with one critical weakness

* **Insufficient Key Size** Are you running on all 8 cores? This small key is factorable on a PC with an efficient implementation

* **Elliptic Curve Private Key Recovery** Given the public parameters of an elliptic curve, recover the poorly chosen private key

* **Monoalphabetic Cipher** Monoalphabetic ciphers leak information. Can you recover it?

* **Factoring RSA With CRT Optimization** Recover a RSA private key when an optimization goes wrong

* **Rainbow Table Hash Chain** Can you use a rainbow table to recover a password?

* **ECDSA Nonce Recovery** Nonce reuse leading to private key recovery, this time with elliptic curves

* **Intro to Hashing** Hashing is a vital concept in cryptography

* **Intro to PGP** Can you use PGP programatically?

* **Intro to RSA** Learn the basics of a common public key cryptosystem

* **CCA on Textbook RSA** Turns out padding is important

* **Fast Hashing Passwords** Cryptographic hash functions shouldn't be used to hash passwords directly

* **Salt Alone Won't Save You** Salting password hashes is important, but not enough on it's own