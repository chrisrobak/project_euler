"""
The sum of the swuares of the first ten natural numbers is:
1*1 + 2*2 + ... + 10*10 = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10) * (1 + 2 + ... + 10) = 55 * 55 = 3025

Hence the difference between the sum of the squares of the first tne
natural numbers and the square of the sum is:

3025 - 385 = 2460.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.

Usage:
    problem_6.py <max_number> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt


def get_sum_of_squares(max_num):
    answer = 0
    for x in xrange(1, max_num + 1):
        answer += x*x
    return answer


def get_square_of_sum(max_num):
    answer = 0
    for x in xrange(1, max_num + 1):
        answer += x
    return answer * answer


def run(max_num):
    sum_of_squares = get_sum_of_squares(max_num)
    square_of_sum = get_square_of_sum(max_num)
    return square_of_sum - sum_of_squares


if __name__ == '__main__':
    args = docopt(__doc__)
    max_num = int(args['<max_number>'])
    difference = run(max_num)
    print "Answer: %d" % difference
