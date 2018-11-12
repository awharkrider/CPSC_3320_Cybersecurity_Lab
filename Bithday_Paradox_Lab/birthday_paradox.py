"""
Aaron Harkrider
"""

import argparse
import random
import math


def main():
    print("Starting the Birthday paradox program")

    #  Parse in arguments from the cmd line
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--t_people', type=int, default=23,
                        help="number of people to compute birthdays for")
    parser.add_argument('-i', '--iterations', type=int, default=10000,
                        help="number of times to run")
    args = parser.parse_args()

    t = int(args.t_people)

    # Calculate the probability of a collision
    prob_no_collision = math.exp(-t * (t - 1) / (2 * 365))
    prob_of_collision = 1 - prob_no_collision

    print("Probability of collision {}".format(prob_of_collision))

    collision_count = 0

    # run a number of times
    for j in range(int(args.iterations)):
        birthdays = []
        # Uniformly assign birthdays (assume 365 days in a year) to t people.
        for i in range(int(t)):
            birthdays.append(random.randint(1, 365))

        # check for collision
        is_collision = len(set(birthdays)) != len(birthdays)
        if is_collision:
            collision_count += 1

    print("There were {} collisions".format(collision_count))
    print("Probability running {} times was {}".format(args.iterations, (collision_count / int(args.iterations))))


# Standard boilerplate to call the main function, if executed
if __name__ == '__main__':
    main()
