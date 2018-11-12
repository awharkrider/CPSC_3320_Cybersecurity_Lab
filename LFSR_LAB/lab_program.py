"""
Author: Aaron Hakrider
Date: 9/27/18
Worked with Joy Shaffer for assistance

"""

from LFSR_LAB import lfsr
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n_bits", type=int, help="number of bits")
    args = parser.parse_args()

    # call my program
    output = my_program(args.n_bits)
    print(output)
    print("percentage: ", output * 100)


def my_program(n_bits):
    """
    The program should take, as positional argument,
     the number of bits to generate and print out the percentage of 1s in the sequence.
     (0, 1, 2, 7, 128)
    :param n_bits: number of bits to generate and print out
    :return:
    """
    c = 1 | (1 << 1) | (1 << 2) | (1 << 7)
    s = int('A' * 32, 16)  # hex number

    mylfsr = lfsr.LFSR(c, s)

    count_ones = 0
    for _ in range(n_bits):
        count = mylfsr.cycle()
        if count == 1:
            count_ones += 1

    return count_ones / n_bits


# Standard boilerplate to call the main function, if executed
if __name__ == '__main__':
    main()
