# Elliptic Curve Laboratory Assignment

## Purpose
The purpose of this lab is to help demystify elliptic curve cryptography.  You will learn that it is relatively easy to implement ECC and perform ECDH and ECDSA that actually match the verified implementation in OpenSSL and other software.  In other words for ECC there is no other "magic" or steps necessary to implement ECC than what you have already learned.

## Details
For this lab you will write Python code that will implement point addition (doubling and regular addition) and point multiplication by a scalar using the double and add algorithm.  Your implementation should support arbitrary prime elliptic curves as described in the textbook.  You need to verify your implementation first by using the small example curve worked out in the textbook.  After you have a working implementation you will try your implementation on the NIST P-256 curve (aka SECP256R1).  You will be comparing your implementation to the python cryptography package.  This python package uses OpenSSL as the default backend so technically you will be comparing your implementation to OpenSSL.  You will need the python [cryptography](https://cryptography.io/en/latest/) package.

1) (5 points) Implement addition and doubling on an elliptic curve using the native Python integers.  
2) (5 points) Implement point multiplication.
3) (5 points) Find the constants to implement the NIST P-256 curve and call the instance of the curve "MyP256".
4) (5 points) Implement the keygen(), sign(), and verify() from the ECDSA algorithm.

### Useful links and hints
* [ECC documentation](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/) for the python cryptography package
* You can get the parameters for the NIST P-256 elliptic curve from "nist-routines.pdf" and tests for ECDSA are in "ECDSA_Prime.pdf"

## Submission
Please commit and push your source code before the due date.  The tests should all pass when run with py.test.  The code should be well documented.
