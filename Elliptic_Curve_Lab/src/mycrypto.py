'''simple modular arithmetic and extension field math
NOTE: Written by Dr. Tarplee
'''

__all__ = [
    'egcd', 'gcd', 'modinv',
    'multiply_gf_bin_ext',
    'reduce_gf_bin_ext',
]

def egcd(a, b):
    '''Extended euclidean algorithm of to compute the GCD of `a` and `b`
    returns gcd, s, t
    '''
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def gcd(a, b):
    '''The greatest common divisor (GCD) of `a` and `b`'''
    return egcd(a, b)[0]


def modinv(a, m):
    '''inverse of a mod m'''
    a %= m
    g, s, t = egcd(m, a)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return t % m


def test_gcd():
    assert gcd(84, 30) == 6
    assert gcd(973, 301) == 7
    assert gcd(10, 15) == 5
    assert gcd(50, 75) == 25


def test_egcd():
    # g, s, t
    assert egcd(973, 301) == (7, 13, -42)
    assert egcd(67, 12) == (1, -5, 28)


def text_modinv():
    assert modinv(12, 67) == 28
    assert modinv(3, 26) == 9


'''
In GF(2^m) addition (and subtraction) is just bitwise XOR 

so a + b is computed as a^b in GF(2^m)
'''

def multiply_gf_bin_ext(a, b):
    '''
    multiply two numbers in GF(2^m)
    returns the product
    '''
    t = 0
    for i in range(b.bit_length()):
        # print("i", i, b & (1 << i))
        if b & (1 << i):
            # print('set', a << i)
            t ^= a << i

    return t

def reduce_gf_bin_ext(a, m):
    '''
    compute the division of a by m in GF(2^n)
    same as reducing a modulo the polynomial m

    returns both the quotient and the remainder
    '''
    rem = a
    quot = 0
    i = a.bit_length()
    while True:
        # print("i", i)
        tmp = rem.bit_length()
        q = rem.bit_length() - m.bit_length()
        # print("q", q)
        if q < 0:
            break
        quot ^= 1 << q
        # the slow way
        # rem ^= multiply_gf_bin_ext(m, 1 << q)
        # the fast way using the special case
        rem ^= m << q
        #print(bin(quot), bin(rem))
        assert rem.bit_length() < tmp

    assert multiply_gf_bin_ext(quot, m) ^ rem == a
    return quot, rem

def test_multiply_gf_bin_ext():
    assert multiply_gf_bin_ext(0b110, 0b101) == 0b11110

def test_reduce_gf_bin_ext():
    assert reduce_gf_bin_ext(0b11110, 0b1011) == (0b11, 0b11)
    assert reduce_gf_bin_ext(0b10101, 0b1011) == (0b10, 0b11)

'''
import codecs
codecs.encode(b, 'hex')
bytes.fromhex(salt_str)

def bytes_to_hex(b):
    return ''.join('{:02x}'.format(x) for x in b)

modular exponentiation can be done with pow(a, b, m) for (a**b) %m
'''
