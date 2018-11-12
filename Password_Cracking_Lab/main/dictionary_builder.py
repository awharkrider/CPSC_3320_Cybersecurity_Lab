"""
This utils Create a master dictionary file with words padded to a length of 8

"Stores the words of length 8 or words of 5-7 padded to 8
@author Aaron Harkrider
@date 10-29-18

Change Log updated 11-07-18:
-renamed
- improved usability
- added ability build dictionary subsets by letter
- Fixed bug: made the word go to lowercase
    - implemented optional argument to build a dictionary consisting of only the uppercase letters

"""

import argparse


def main():
    #  Parse in arguments from the cmd line
    parser = argparse.ArgumentParser(
        description="Create a dictionary files with words padded to a length of 8 split into subsets to thread faster")
    parser.add_argument("word_length",
                        help="param to limit the words to only those of a particular length before padding. "
                             "Words of length 8 or words of 5-7 that will be padded to 8")
    parser.add_argument("-d", "--dictionary_name", metavar='', default="master_dictionary.txt",
                        help="Name of the new dictionary file to store the selected words. "
                             "(defaults to master_dictionary.txt)")

    # The -u param is needed because in an early version of the program I did not put all words to lowercase
    parser.add_argument("-u", "--upper_case_words_only", metavar='', default="false",
                        help="Determines if it should sort out only the words with an uppercase letter. "
                             "(Defaults to false and will turn all words into lower case.)")
    parser.add_argument("-l", "--alphabet_letter", metavar='', default="all",
                        help="If set will only build a dictionary with words starting with the indicated letter. "
                             "(Defaults to the entire alphabet)")
    args = parser.parse_args()

    dictionary_name = "../dictionaries/" + args.dictionary_name
    master_dictionary = open(dictionary_name, "w+")  # creating a file if it doesn't exist
    print("Writing dictionary words to file: {}\n".format(dictionary_name))

    # read in word_file
    with open("../dictionaries/words") as word_file:

        for line in word_file:

            word = line.strip()

            if len(word) != int(args.word_length):
                continue

            if args.upper_case_words_only != "false":
                if word[0].islower():
                    continue

            word = word.lower()

            if args.alphabet_letter != "all":
                # If are sorting on a specific alphabet letter
                if not word.startswith(args.alphabet_letter):
                    # if the starting character of the word is not of the letter we are sorting on skip it.
                    continue

            # if the word length is less then 8 add padding
            if len(word) == 8:
                print("No padding needed for '{}'".format(word))
                master_dictionary.write(word + '\n')
            elif len(word) == 7:
                print("Adding 1 digit of padding to '{}'".format(word))
                for i in range(10):
                    # add the 0-9 as padding
                    master_dictionary.write(word + str(i) + '\n')
            elif len(word) == 6:
                print("Adding 2 digit of padding to '{}'".format(word))
                for i in range(10):
                    # add the 0-9 as padding
                    # e.g. spider0
                    padded_word1 = word + str(i)
                    for j in range(10):
                        # add the 0-9 as padding
                        # e.g spider00
                        # then spider01
                        # and so on
                        master_dictionary.write(padded_word1 + str(j) + '\n')
            elif len(word) == 5:
                print("Adding 3 digit of padding to '{}'".format(word))
                for i in range(10):
                    # add the 0-9 as padding
                    padded_word1 = word + str(i)
                    for j in range(10):
                        # add the 0-9 as padding
                        padded_word2 = padded_word1 + str(j)
                        for k in range(10):
                            # add the 0-9 as padding
                            master_dictionary.write(padded_word2 + str(k) + '\n')

    master_dictionary.close()


# Standard boilerplate to call the main function, if executed
if __name__ == '__main__':
    main()
