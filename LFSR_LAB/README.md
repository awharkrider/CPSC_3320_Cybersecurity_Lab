# LFSR_LAB
- Due: 5 pm Oct 3rd, 2018
- Points: 10

## Objective
Learn some "bit fiddling" in python while implementing a weak random number generator.

## Resources
https://wiki.python.org/moin/BitManipulation (Links to an external site.)

## Procedure
Implement the LFSR as a class in python.  The constructor should take two arguments.  The first an integer representing the coefficients of the characteristic polynomial for the LFSR.  The second argument should be an integer representing the seed of the LFSR.  The LFSR class should have a method called "cycle" to generate a single bit each time it is called.  
Unit test your code against the examples provided in the book and the homework.  Your unit test must be compatible with py.test.
Write a program that uses the LFSR with the primitive polynomial of order 128 from table 2.3.  The seed is given by the hexadecimal number which is equal to your desired grade in your classes (i.e., all As).  The program should take, as positional argument, the number of bits to generate and print out the percentage of 1s in the sequence.
Run the LFSR for various number of iterations and observe the percentage of 1s.

## Submission
Submit your code and the sample output from the unit tests and the program.  