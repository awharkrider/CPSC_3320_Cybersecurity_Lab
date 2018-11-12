"""
@author Aaron Harkrider
@date 10-29-18



Change Log updated 11-07-18:
- reduced cluttter
- improved runtime
- improved usability
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import argparse
import time


def main():
    print("Starting Aaron's password cracking program.\n")

    #  Parse in arguments from the cmd line
    parser = argparse.ArgumentParser()
    parser.add_argument("dictionary_file", default="master_dictionary.txt",
                        help="File of dictionary words to use to crack the digests, "
                             "(Default to master_dictionary.txt)")
    parser.add_argument("-c", "--cracked_digests", default="master_cracked_digests.csv",
                        help="stores the digests found with matched password, "
                             "(Defaults to master_cracked_digests.csv)")
    parser.add_argument('-u', '--uncracked_digests', default="uncracked_digests.csv",
                        help="File of un-cracked password digests, "
                             "(Defaults to uncracked_digests.csv)")

    args = parser.parse_args()

    print("Reading in un-cracked password digests")
    # Read in the un-cracked password digests from file
    salty_digests = []
    with open(args.uncracked_digests) as digests:
        for line in digests:
            salty_digests.append(line)

    found_passwords = []
    with open(args.cracked_digests, 'r') as found_file:

        # remove found digest from the digest array
        print("...Improving search time by removing already cracked digests.\n")
        for line in found_file:
            found_password, found_salt, found_digest = line.strip().split(',')

            # saving found passwords so we can skip words in our dictionary if we already cracked them
            found_passwords.append(found_password)

            found_salty_digest = found_salt + ',' + found_digest + '\n'  # building line that matches the digest file
            if found_salty_digest in salty_digests:
                salty_digests.remove(found_salty_digest)

    found_file.close()

    print("Starting password brute force search!\n")
    then = time.time()  # Time before the operations start

    print("Opening dictionary: ", args.dictionary_file)
    # read in dictionary_file
    with open(args.dictionary_file) as dict_file:

        first_letter = "-"

        for line in dict_file:
            word = line.strip()
            if word in found_passwords:
                # Word already cracked moving on
                continue

            if not word.startswith(first_letter):
                first_letter = word[0]
                print("Starting the '{}' words\n".format(first_letter))

            # attempting to crack
            for digest_line in salty_digests:

                salt, digest = digest_line.strip().split(',')

                backend = default_backend()

                # Salts should be randomly generated
                salt_bytes = bytes.fromhex(salt)

                # derive
                kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                                 length=32,
                                 salt=salt_bytes,
                                 iterations=100000,
                                 backend=backend)

                key = kdf.derive(word.encode('utf-8'))

                digest_bytes = bytes.fromhex(digest)

                # check if we found a match
                if key == digest_bytes:
                    print('FOUND digest for {}.\n'.format(word))
                    cracked = salt + ',' + digest + '\n'

                    print(word + ',' + cracked)
                    with open(args.cracked_digests, 'a+') as cracked_file:
                        cracked_file.write(word + ',' + cracked)

                    # removing the cracked digest from search space
                    salty_digests.remove(cracked)

    now = time.time()  # Time after it finished
    print("It took: ", now - then, " seconds to iterate through the entire dictionary and digests.\n")


# Standard boilerplate to call the main function, if executed
if __name__ == '__main__':
    main()
