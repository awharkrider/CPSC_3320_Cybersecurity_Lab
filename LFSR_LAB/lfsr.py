"""
Author: Aaron Harkrider
Date: 9/27/18
# Linear Feed Back Shift Register


Implement the LFSR as a class in python.  The constructor should take two arguments.  
    * The first an integer representing the coefficients of the characteristic polynomial for the LFSR.  
    * The second argument should be an integer representing the seed of the LFSR.  
The LFSR class should have a method called "cycle" to generate a single bit each time it is called.


# Unit test your code against the examples provided in the book and the homework.  Your unit test must be compatible with py.test.
# Write a program that uses the LFSR with the primitive polynomial of order 128 from table 2.3. 
 
The seed is given by the hexadecimal number which is equal to your desired grade in your classes (i.e., all As).  
The program should take, as positional argument, the number of bits to generate and print out the percentage of 1s in the sequence.
# Run the LFSR for various number of iterations and observe the percentage of 1s.


    # m =3
    # p = 0b101
    # s = 0b100

    #   s1 = 0
    #   s2 = 1
    #   s3 = 0
    #   s4 = 1
    #   s5 = 1
    #   s6 = 1
"""


class LFSR:
    def __init__(self, p, seed):
        """
        Linear Feedback Shift Register

        :param p: an integer representing the coefficients of the characteristic polynomial for the LFSR
        :param seed: an integer representing the seed of the LFSR
        """
        self.p = p
        self.s = seed  # Thing we are going to flip flop
        self.nbits = seed.bit_length()
        print(self.nbits)

    def cycle(self):
        """
        generate a single bit each time it is called
         uses bit wise operation to manipulate s
        :return: the new bit
        """

        new_bit = self.s & 1  # get the last bit

        z = self.s & self.p  # Bitwise AND

        # xor the individual bits
        r = self.xor_reduce(z)

        # bit shift
        # stick z on the front of s
        self.s = (self.s >> 1) | (r << (self.nbits - 1))  # short hand

        return new_bit

    def xor_reduce(self, z):
        """
        bitwise xored with itself
        :param z:
        :return: bool
        """
        temp = False
        for i in range(z.bit_length()):
            temp = temp ^ bool((z & (1 << i)))
        return temp


def test_lfsr():
    """
    unit test of lfsr
    """
    p = 0b101
    seed = 0b100
    mylfsr = LFSR(p, seed)
    assert mylfsr.nbits == 3
    data = [mylfsr.cycle() for _ in range(7 * 2)]
    assert data == [0, 0, 1, 1, 1, 0, 1] * 2
