"""
Author: Aaron Hakrider
Date: 9/27/18
"""
from LFSR_LAB import lfsr


def test_lfsr():
    p = 0b101
    seed = 0b100
    mylfsr = lfsr.LFSR(p, seed)
    assert mylfsr.nbits == 3
    data = [mylfsr.cycle() for _ in range(7 * 2)]
    assert data == [0, 0, 1, 1, 1, 0, 1] * 2
