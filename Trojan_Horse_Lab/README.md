# Trojan_Horse_Lab
- Due: 5 pm Thursday November 15th, 2018
- Points: 10

## Objective
This lab is intended to allow you to apply the knowledge you have gained this semester and to open your eyes to the power you hold by submitting source code to professors.

## Procedure
Build a trojan horse that gains access to a file on cyber.anderson.edu.  The file under attack is the grade book for this assignment.  You must enter name and grade (I hope you give yourself a good grade) correctly in the file that is protected by UNIX file permissions.  Please do not modify anyone else's grade.  You need to show the professor how your attack works to receive credit (which you can do during the attack).

Write a unit test in a file called "$USER_test.py" that will run automatically with py.test and put it in a directory called trojan_horse in your home directory.  The "professor" will collect the submissions periodically into a common folder and run py.test to "evaluate your submissions."  Just like regular unit tests, your unit test should take less than a second to execute and not block.  It should also not SEGFAULT or otherwise crash the test runner (i.e., py.test).

## Warning
Obviously never do this (hack the professor's account) without the permission of the professor.

## Submission
Submit your trojan horse source code.  Please heavily document your code and the approach you took to infiltrate the "City of Troy."  Extra points will be given for creative solutions.