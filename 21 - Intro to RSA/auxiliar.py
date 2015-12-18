import itertools as it

# http://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python


# erat3
def prime():
    D = {9: 3, 25: 5}
    yield 2
    yield 3
    yield 5
    MASK = 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in D or (x % 30) not in MODULOS:
                x += 2 * p
            D[x] = p
