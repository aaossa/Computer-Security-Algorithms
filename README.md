# Computer Security Algorithms

Problems related to computer security. Algorithms written in Python. [Follow the Tutorial](https://id0-rsa.pub/)

### Main topics (Tags)

* **RSA:** RSA stands for [*Rivest-Shamir-Adleman*](https://en.wikipedia.org/wiki/RSA_(cryptosystem)). Is a widely used public-key cryptosystem "based on the practical difficulty of factoring the product of two large prime numbers" ([RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)))

* **PublicKey-Crypto:**

* **Hashing:** A [*hash function*](https://en.wikipedia.org/wiki/Hash_function) maps data of arbitrary size to data of fixed size. An [ideal hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function) maps randomly, avoid colissions and is impossible to invert.

* **Symmetric-Crypto:**

* **Classical-Crypto:**

* **Passwords:**

* **AES:**

* **Tutorial:**

* **Bitcoin:**

* **PGP:** PGP stands for [*Pretty Good Privacy*](https://en.wikipedia.org/wiki/Pretty_Good_Privacy). Is a program used to facilitate encrypt and decrypt your mail. PGP "has proven itself quite capable of resisting even the most sophisticated forms of analysis" ([PGP faqs](http://www.faqs.org/faqs/pgp-faq/part1/))

* **ECC:**

* **Factoring:**

* **OpenSSL:**

* **PRNG:**

### Solved Problems

* **Hello PGP** Use PGP programatically. Recover the message encrypted with a single English word.

* **Hello Bitcoin** Do you know how bitcoin addresses are constructed?

* **Hello OpenSSL** Can you read and use an OpenSSL RSA key?

* **AES-CTR with Nonce Reuse** Can you exploit a reused nonce?

* **Affine Cipher** Can you brute force this classical cipher?

* **Double Strength Affine** A slight security upgrade, is it enought?

* **Ps and Qs** RSA keys generated with one critical weakness

* **Insufficient Key Size** Are you running on all 8 cores? This small key is factorable on a PC with an efficient implementation

* **Elliptic Curve Private Key Recovery** Given the public parameters of an elliptic curve, recover the poorly chosen private key

* **Håstad's Broadcast Attack** RSA with a small exponent is fast to compute but it has a serious weakness

* **Monoalphabetic Cipher** Monoalphabetic ciphers leak information. Can you recover it?

* **Playfair** This bigram cipher is a bit trickier...

* **Factoring RSA With CRT Optimization** Recover a RSA private key when an optimization goes wrong

* **Rainbow Table Hash Chain** Can you use a rainbow table to recover a password?

* **ECDSA Nonce Recovery** Nonce reuse leading to private key recovery, this time with elliptic curves

* **Intro to Hashing** Hashing is a vital concept in cryptography

* **Intro to PGP** Can you use PGP programatically?

* **Intro to RSA** Learn the basics of a common public key cryptosystem

* **CBC Padding Attack** CBC is one of the best modes of operation for block ciphers, but even leaking a tiny amount of information is enough to completely undermine its security

* **CCA on Textbook RSA** Turns out padding is important

* **Fast Hashing Passwords** Cryptographic hash functions shouldn't be used to hash passwords directly

* **Salt Alone Won't Save You** Salting password hashes is important, but not enough on it's own

* **Cut and Paste Attack On AES-ECB** Create a valid ciphertext without knowledge of the key using some copypaste

* **Insecure PRNG** Using a PRNG that isn't proven to be cryptographically secure is a recipe for disaster

* **Bad Entropy** It's easy to generate bad symmetric keys

* **Caesar** Should probably stick to the salad

### Unsolved Problems

* **Bleichenbacher's CCA2 on RSA** 14

* **CRIMEs against TLS** 20

* **CBC Padding Attack** 22

* **Breaking PDF Passwords** 29

* **Backdoored PRNG** 31

* **Vigenère** 33

* **Rail Fence** 34

* **Vigenère + Rail Fence** 35

* **Not So Safe Primes** 37