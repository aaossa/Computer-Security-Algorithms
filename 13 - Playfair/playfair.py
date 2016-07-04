from fitness_measure import ngram_score as ns
from math import exp
from os.path import abspath
from pycipher import Playfair
from random import randint, random, sample
from string import ascii_uppercase


# Problem
# https://id0-rsa.pub/problem/13/

# Resources
# http://practicalcryptography.com/ciphers/playfair-cipher/
# https://en.wikipedia.org/wiki/Simulated_annealing
# https://en.wikipedia.org/wiki/Genetic_algorithm
# http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-playfair/
# http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/

# http://www.ouah.org/acmken.htm

with open("ciphertext") as f:
    CIPHERTEXT = f.read()


def swap_parent(parent):
    parent = list(parent)
    a = randint(0, len(parent) - 1)
    _b = randint(0, len(parent) - 2)
    b = _b + 1 if _b >= a else _b
    parent[a], parent[b] = parent[b], parent[a]
    return "".join(parent)


# 1. Generate a random key, called the 'parent', decipher
# the ciphertext using this key
parent = ''.join(sample(ascii_uppercase, 26)).replace("J", "")
parent = "GONPLRSHEAIKTDMBCUQFYWXZV"
parent_deciphered = Playfair(parent).decipher(CIPHERTEXT)

# 2. Rate the fitness of the deciphered text, store the result
fitness = ns('english_bigrams.txt')
parent_fitness = fitness.score(parent_deciphered)

# 3. for(TEMP = 10;TEMP >= 0; TEMP = TEMP - STEP)
TEMP = 10
STEP = 1
maximum_fitness = parent_fitness
while TEMP >= 1:
    TEMP = TEMP - STEP
    print("Current temperature: {}".format(TEMP))
    # for (count = 50,000; count>0; count--)
    for count in reversed(range(50000)):
        # Change the parent key slightly (e.g. swap two
        # characters in the key at random) to get child key,
        child = swap_parent(parent)
        # Measure the fitness of the deciphered text
        # using the child key
        child_deciphered = Playfair(child).decipher(CIPHERTEXT)
        child_fitness = fitness.score(child_deciphered)
        # set dF = (fitness of child - fitness of parent)
        dF = child_fitness - parent_fitness
        # If dF > 0 (fitness of child is higher than parent key),
        if dF > 0:
            # set parent = child
            parent = child
            parent_fitness = child_fitness
            parent_deciphered = child_deciphered
            print("New parent: {} ({})".format(parent_deciphered[:20], parent))
        # If dF < 0 (fitness of child is worse than parent),
        if dF < 0:
            # set parent = child with probability e^(dF/T).
            try:
                prob = exp(dF / TEMP)
                if prob > random():
                    parent = child
                    parent_fitness = child_fitness
                    parent_deciphered = child_deciphered
                    print("Child is worse: {} ({})".format(
                        parent_deciphered[:20], parent))
            except:
                pass


if __name__ == '__main__':
    print(parent)
    print(parent_fitness)
    print(parent_deciphered)

    KEY = "GONPLRSHEAIKTDMBCUQFYWXZV"
    ANSWER = "THEFIRSTSIXTYCHARACTERSISTHESOLUTIONITHANKTHEACMFORTHISAWARD"
