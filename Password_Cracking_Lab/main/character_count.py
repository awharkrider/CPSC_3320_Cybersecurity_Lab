import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="dictionary file .txt")
    args = parser.parse_args()

    # Read in dictionary file
    with open(args.file) as dictionary_file:

        count = [0] * 8

        for line in dictionary_file:
            word = line.strip()

            for j in range(8):
                if len(word) == (j + 1):
                    count[j] += 1

        for i in range(8):
            print("word length: " + str(i + 1) + " count: " + str(count[i]))


# Standard boilerplate to call the main function, if executed
if __name__ == '__main__':
    main()
