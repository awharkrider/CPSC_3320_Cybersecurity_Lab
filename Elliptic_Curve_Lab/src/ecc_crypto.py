"""
Aaron Harkrider
Date: 11-30-2018

Collaborated with: kebixler, jeshaffer, amwallace
"""

from mycrypto import modinv
import random


class EllipticCurve:
    def __init__(self, p, a, b):
        """Example 9.5 from the textbook"""
        self.natural = "theta natural element on curve"
        self.p = p
        self.a = a
        self.b = b

    def add(self, p1, p2):
        """Point Addition and Point Doubling"""
        if p1 == self.natural:
            return p2
        if p2 == self.natural:
            return p1

        x1, y1 = p1
        x2, y2 = p2

        if p1 != p2:
            """Point Addition"""
            if x2 == x1:
                return self.natural
            s = (y2 - y1) * modinv((x2 - x1), self.p)
        else:
            """Point Doubling"""
            if y1 == 0:
                return self.natural
            s = ((3 * x1 ** 2) + self.a) * modinv((2 * y1), self.p)

        x3 = (s ** 2 - x1 - x2) % self.p
        y3 = (s * (x1 - x3) - y1) % self.p

        return x3, y3

    def multiply(self, d, P):
        """Point Multiplication"""
        t = d.bit_length() - 1
        T = P

        for i in range(t - 1, -1, -1):
            T = self.add(T, T)
            if d & (1 << i):
                T = self.add(T, P)

        return T


# MyP256, keygen, sign, verify

def curve_myP256():
    """ nist-routines Curve P–256 parameters """
    p = int("ffffffff00000001000000000000000000000000ffffffffffffffffffffffff", 16)
    a = int("ffffffff00000001000000000000000000000000fffffffffffffffffffffffc", 16)
    b = int("5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b", 16)

    ec = EllipticCurve(p, a, b)

    xG = int("6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296", 16)
    yG = int("4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5", 16)

    # Adding variables to Elliptic Curve P-256
    ec.A = (xG, yG)
    ec.q = int("ffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551", 16)
    ec.P = ec.A
    return ec


""" Exporting as  a Class"""
MyP256 = curve_myP256()


def keygen(curve):
    """page 283 of Understanding cryptography"""
    d = random.randint(1, curve.q)

    B = curve.multiply(d, curve.A)

    return d, B


def sign(curve, h_x, priv_key):
    """page 283 of Understanding cryptography"""
    kE = random.randint(1, curve.q)

    R = curve.multiply(kE, curve.A)

    r = R[0]

    s = (h_x + priv_key * r) * modinv(kE, curve.q)
    return r, s


def verify(curve, h_x, pub_key, rs):
    """page 284 of Understanding cryptography"""
    w = modinv(rs[1], curve.q)
    u1 = w * h_x % curve.q
    u2 = w * rs[0] % curve.q

    # scalar multiplication
    P = curve.add(curve.multiply(u1, curve.A), curve.multiply(u2, pub_key))
    return P[0] == rs[0] % curve.q
