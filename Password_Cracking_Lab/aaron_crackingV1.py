"""
Version one of my cracking.py

"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import argparse
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dictionary_file", default="words", help="dictionary file, (defaults to words) ")
    parser.add_argument("passwords_file", default=".awharkrider_digests.csv",
                        help="password file of .csv (defaults to .awharkrider_digests.csv)")
    parser.add_argument("cracked_digests", default="cracked_digests.csv",
                        help="stores the digests found with matched password (defaults to cracked_digests.csv)")

    args = parser.parse_args()

    # read in dictionary file
    dictionary = []
    with open(args.dictionary_file) as dict_file:
        for line in dict_file:
            # if the line == length 8
            if len(line.strip()) == 8:
                dictionary.append(line.strip())

    # Read in passwords description file
    salty_digests = []
    with open(args.passwords_file) as passwords:
        for line in passwords:
            salty_digests.append(line)

    with open(args.cracked_digests, 'r') as found_file:

        for line in found_file:

            # remove found digest from the digest array
            found_salt, found_digest, found_password = line.strip().split(',')

            found_salty_digest = found_salt + ',' + found_digest + '\n'
            if found_salty_digest in salty_digests:
                print('Digest already cracked removing it. found_salty_digest = {}'.format(found_salty_digest))
                salty_digests.remove(found_salty_digest)

        found_file.close()

    then = time.time()  # Time before the operations start
    new_found = crack_password(dictionary, salty_digests)
    now = time.time()  # Time after it finished
    print("It took: ", now - then, " seconds to iterate through the entire dictionary and digests.\n")
    with open(args.digests_found, 'a') as found_file:
        for password in new_found:
            found_file.write(password)


def crack_password(dictonary, digests):
    new_found = []

    for word in dictonary:
        for line in digests:
            then = time.time()  # Time before the operations start

            salt, digest = line.strip().split(',')

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

            if key == digest_bytes:
                elapsed_time = time.time() - then

                print('FOUND!  It took "{}" seconds to crack this password.\n'.format(elapsed_time))
                found = salt + ',' + digest
                digests.remove(line)
                new_found.append(found + ',' + word + '\n')
                print('digest: {},\n digest_bytes: {},\n word: {}\n'.format(digest, digest_bytes, word))

    return new_found


# Standard boilerplate to call the main function, if executed
if __name__ == '__main__':
    main()
