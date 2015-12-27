class ECPoint():

    def __init__(self, x, y, curve, name=None):
        self.x = x
        self.y = y
        self.curve = curve
        self.name = name

    def __add__(self, other):
        p = self.curve.p
        x_p, y_p = self.x, self.y
        x_q, y_q = other.x, other.y
        s = ((y_q - y_p) * self.__modinv((x_q - x_p), p)) % p
        x_r = (pow(s, 2) - x_p - x_q) % p
        y_r = (s * (x_p - x_r) - y_p) % p
        return ECPoint(x_r, y_r, self.curve)

    def __eq__(self, other):
        x_coord = bool(self.x == other.x)
        y_coord = bool(self.y == other.y)
        if self.curve != other.curve:
            print("WARNING: These point are not on the same curve")
        return (x_coord and y_coord)

    def __mul__(self, value):
        # https://github.com/AntonKueltz/elliptic-curve-math/blob/master/src/ecmath.py
        R0 = ECPoint(0, 0, self.curve)
        R1 = ECPoint(self.x, self.y, self.curve)
        kbin = bin(value).replace('0b', '')

        for i in range(0, len(kbin)):
            if kbin[i] == '0':
                R1 = R0 + R1
                R0 = R0.__double_point()
            else:
                if (R0.x, R0.y) == (0, 0):
                    R0 = ECPoint(R1.x, R1.y, self.curve)
                else:
                    R0 = R0 + R1
                R1 = R1.__double_point()

        return R0

    def __neg__(self):
        return ECPoint(self.x, (-1 * self.y) % p, self.curve)

    def __repr__(self):
        if self.name is None:
            return "Point: ({}, {})".format(self.x, self.y)
        else:
            return "Point '{}': ({}, {})".format(self.name, self.x, self.y)

    def __double_point(self):
        p = self.curve.p
        s = ((3 * pow(self.x, 2) + self.curve.a) *
             self.__modinv(2 * self.y, p)) % p
        x_r = (pow(s, 2) - 2 * self.x) % p
        y_r = (s * (self.x - x_r) - self.y) % p
        return ECPoint(x_r, y_r, self.curve)

    def __egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.__egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def __modinv(self, a, m):
        while a < 0:
            a += m
        g, x, y = self.__egcd(a, m)
        if g != 1:
            print("a = {}".format(a))
            print("m = {}".format(m))
            print("g = {}".format(g))
            raise Exception('modular inverse does not exist')
        else:
            return x % m


class EllipticCurve():

    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def generator_point(self, *args):
        if len(args) == 1:
            self.__generator_point_ecpoint(*args)
        elif len(args) == 2:
            self.__generator_point_coordinates(*args)
        else:
            print("WARNING: Wrong number of parameters (1 -> ECPoint, 2 -> int, int)")

    def public_key(self, *args):
        if len(args) == 1:
            self.__public_key_ecpoint(*args)
        elif len(args) == 2:
            self.__public_key_coordinates(*args)
        else:
            print("WARNING: Wrong number of parameters (1 -> ECPoint, 2 -> int, int)")

    def __generator_point_ecpoint(self, ecpoint):
        if self.__point_on_curve(ecpoint.x, ecpoint.y):
            self.G = ecpoint
        else:
            print("WARNING: This point is not on the curve")

    def __generator_point_coordinates(self, x, y):
        if self.__point_on_curve(x, y):
            self.G = ECPoint(x, y, self)
        else:
            print("WARNING: This point is not on the curve")

    def __point_on_curve(self, x, y):
        l_side = pow(y, 2, self.p)
        r_side = (pow(x, 3) + self.a * x + self.b) % self.p
        return bool(l_side == r_side)

    def __public_key_ecpoint(self, ecpoint):
        if self.__point_on_curve(ecpoint.x, ecpoint.y):
            self.Q = ecpoint
        else:
            print("WARNING: This point is not on the curve")

    def __public_key_coordinates(self, x, y):
        if self.__point_on_curve(x, y):
            self.Q = ECPoint(x, y, self)
        else:
            print("WARNING: This point is not on the curve")

if __name__ == '__main__':
    a = int('-0x3', 16)
    b = int('0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b', 16)
    p = int('0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff', 16)

    EC = EllipticCurve(a, b, p)

    gx = int('0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296', 16)
    gy = int('0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5', 16)

    G = ECPoint(gx, gy, EC)
    EC.generator_point(G)

    ds = [
        1,
        2,
        112233445566778899,
        12078056106883488161242983286051341125085761470677906721917479268909056
    ]

    results = [
        (int('6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296', 16),
         int('4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5', 16)),
        (int('7CF27B188D034F7E8A52380304B51AC3C08969E277F21B35A60B48FC47669978', 16),
         int('07775510DB8ED040293D9AC69F7430DBBA7DADE63CE982299E04B79D227873D1', 16)),
        (int('339150844EC15234807FE862A86BE77977DBFB3AE3D96F4C22795513AEAAB82F', 16),
         int('B1C14DDFDC8EC1B2583F51E85A5EB3A155840F2034730E9B5ADA38B674336A21', 16)),
        (int('5E6C8524B6369530B12C62D31EC53E0288173BD662BDF680B53A41ECBCAD00CC', 16),
         int('447FE742C2BFEF4D0DB14B5B83A2682309B5618E0064A94804E9282179FE089F', 16))
    ]

    for i in range(len(ds)):
        F = G * ds[i]
        print(F)
        print(F.x == results[i][0], F.y == results[i][1])

        print()
