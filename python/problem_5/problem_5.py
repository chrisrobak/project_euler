"""
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?

Usage:
    problem_5.py <max_number> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt


def get_smallest_multiple_for_factorial(max_num):
    # start from the top and decrement
    current_number = max_num
    while current_number > 1:
        # must be multiple of current number, so extend by it
        next_num = max_num
        # max_num is current number to check, extend it
        # if not divisble yet
        while (max_num % current_number != 0):
            max_num += next_num
        # next number down the sequence..
        current_number = current_number - 1
    return max_num


if __name__ == '__main__':
    args = docopt(__doc__)
    max_num = int(args['<max_number>'])
    print "Smallest multiple for: %s" % [x for x in xrange(1, max_num + 1)]
    smallest_multiple = get_smallest_multiple_for_factorial(max_num)
    print "Smallest multiple: %d" % smallest_multiple
