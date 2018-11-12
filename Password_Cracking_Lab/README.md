# CPSC3320_Lab_Password_Cracking
Python program to crack given hashed passwords.


The password file has the salt then the PBKDF2 digest on each line encoded in hexadecimal.  The passwords are encoded in UTF-8 but they only contain ASCII characters so the encoding can be considered ASCII as well.

To reduce the search space all passwords are exactly 8 characters in length.  The passwords only contain lowercase letters (uppercase letters in the dictionary are converted to lowercase) and numbers.  The roots of the passwords are from this dictionary.  


## Questions (10 points)
1. Make a table with rows being the word size (1, 2, 3, 4, 5, 6, 7, and 8 letter words) in the provided dictionary.  Add a column that contains the number of words of that length, and another column with the size of the key space (after padding with numbers).
2. What is the size of the overall key space (1 to 8 character words)?
3. What is the size of the key space for words that are 5 to 8 characters?
4. Based on the time to crack a password add a column to the table that computes the monetary cost of searching the space.  Show your equation you used to compute this quantity.

## Passwords Sets
There are different types of passwords in the file (in random order).

1. The password "password" is in the password file so you can verify your code.
2. There are 10 dictionary words (e.g., computer).  One point for each password you crack.
3. There are 10 dictionary words, of 5 to 7 letters, followed by numbers.  (e.g., house423, houses39, compute9) One point for each password you crack. (extra credit)
