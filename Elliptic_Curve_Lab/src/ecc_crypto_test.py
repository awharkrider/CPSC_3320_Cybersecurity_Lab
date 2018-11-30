from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils

P256 = ec.SECP256R1()

from ecc_crypto import EllipticCurve, MyP256, keygen, sign, verify


def test_basic():
    '''Example 9.5 from the textbook'''
    curve = EllipticCurve(17, 2, 2)
    assert curve.add((5, 1), (5, 1)) == (6, 3)
    assert curve.add((6, 3), (5, 1)) == (10, 6)

    tests = [
        (5, 1),
        (6, 3),
        (10, 6),
        (3, 1),
        (9, 16),
        (16, 13),
        (0, 6),
        (13, 7),
        (7, 6),
        (7, 11),
        (13, 10),
        (0, 11),
        (16, 4),
        (9, 1),
        (3, 16),
        (10, 11),
        (6, 14),
        (5, 16),
        curve.natural
    ]
    tmp = curve.natural
    for i, val in enumerate(tests):
        tmp = curve.add(tmp, tests[0])
        assert tmp == val, "tmp = {}, val = {}".format(tmp, val)
        assert curve.multiply(i + 1, tests[0]) == val, "i = {} val = {}".format(i, val)


def test_ecdh():
    '''Test ECDH implementation'''

    # generate my private key
    private_key = ec.generate_private_key(P256, default_backend())

    priv_key = private_key.private_numbers()
    d = priv_key.private_value
    public_key = private_key.public_key()
    pub_key = public_key.public_numbers()

    # generate remote private key (really only want the public key)
    peer_public_key = ec.generate_private_key(P256, default_backend()).public_key()
    peer_pub_key = peer_public_key.public_numbers()

    secret = private_key.exchange(ec.ECDH(), peer_public_key)

    # compute the public key myself
    assert MyP256.multiply(d, MyP256.P) == (pub_key.x, pub_key.y)

    # compute the key exchange myself
    assert MyP256.multiply(d, (peer_pub_key.x, peer_pub_key.y))[0] == int.from_bytes(secret, byteorder='big')


def test_ecdsa():
    '''Test ECDSA compared to cryptograph.io'''
    private_key = ec.generate_private_key(P256, default_backend())

    priv_key = private_key.private_numbers()
    d = priv_key.private_value
    public_key = private_key.public_key()
    pub_key = public_key.public_numbers()

    msg = b"cybersecurity is cool"

    signature = private_key.sign(msg, ec.ECDSA(hashes.SHA256()))

    r, s = utils.decode_dss_signature(signature)
    print("r =", r, "s =", s)

    hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
    hasher.update(msg)
    digest = hasher.finalize()

    h_x = int.from_bytes(digest, byteorder='big')

    valid = verify(MyP256, h_x, (pub_key.x, pub_key.y), (r, s))
    assert valid


def test_ecdsa_full():
    '''Self-test of ECDSA'''
    h_x = 23432423143242342342314312

    priv_key, pub_key = keygen(MyP256)

    # rs is the signature
    rs = sign(MyP256, h_x, priv_key)

    assert verify(MyP256, h_x, pub_key, rs)

    assert not verify(MyP256, h_x, pub_key, (rs[0], rs[1] + 1))
    assert not verify(MyP256, h_x, pub_key, (rs[0] + 1, rs[1]))
    assert not verify(MyP256, h_x + 1, pub_key, rs)
