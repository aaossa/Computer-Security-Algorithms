# Problem
# https://id0-rsa.pub/problem/34/

# Resources
# https://en.wikipedia.org/wiki/Rail_fence_cipher

PT = "WEAREDISCOVEREDFLEEATONCE"
KEY = 3
CT = "WECRL TEERD SOEEF EAOCA IVDEN"


class RailFence:

    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        current, up = 0, False
        fence = list(str() for rail in range(self.key))
        for char in plaintext:
            fence[current] += char
            up = False if not current else True if current == self.key - 1 else up
            current = current - 1 if up else current + 1
        # Partial ciphertext
        pre_ct = "".join(fence)
        # Processed ciphertext
        pro_ct = " ".join(pre_ct[i:i + 5] for i in range(0, len(pre_ct), 5))
        return pro_ct

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.replace(" ", "")
        cicle_length = self.key + self.key - 2
        n_cicles = len(ciphertext) // cicle_length
        extra = len(ciphertext) - n_cicles * cicle_length

        cipherlist = list(ciphertext)
        stack = list()

        head, cipherlist = cipherlist[:n_cicles], cipherlist[n_cicles:]
        if extra:
            head.append(cipherlist.pop(0))
            init_length = len(cipherlist)
        while extra:
            if extra == 1:
                pass
            elif extra == self.key:
                stack.insert(0, cipherlist.pop(-1))
            elif extra < self.key:
                # position = len(head) + 2 * n_cicles * extra
                position = extra * self.key - 2 * len(head)
                stack.insert(0, cipherlist.pop(position))
            else:  # extra > self.key
                difference = extra - self.key
                position = init_length - difference * self.key
                stack.insert(0, cipherlist.pop(position))
            extra -= 1
        cipherlist, tail = cipherlist[:-n_cicles], cipherlist[-n_cicles:]

        parts = list()
        parts.append(head)
        for index in range(0, len(cipherlist), 2 * n_cicles):
            parts.append(cipherlist[index:index + 2 * n_cicles])
        parts.append(tail)

        current, up = 0, False
        output = str()
        for _ in range(sum(len(part) for part in parts)):
            output += parts[current].pop(0)
            up = False if not current else True if current == self.key - 1 else up
            current = current - 1 if up else current + 1

        output += "".join(stack)

        return output

if __name__ == '__main__':
    # Test Vector
    RF = RailFence(KEY)
    enc = RF.encrypt(PT)
    dec = RF.decrypt(CT)
    assert(enc == CT)
    assert(dec == PT)

    # Real case
    with open("ciphertext") as f:
        ct = f.read().replace(" ", "")
    RF = RailFence(60)
    # dec = RF.decrypt(ct)
    # print(dec[:25])

    # Exercise
    for key in range(2, len(ct)):
        rf = RailFence(key)
        try:
            dec = rf.decrypt(ct)
            print(key, dec[:50])
        except Exception as e:
            print(e.args)
