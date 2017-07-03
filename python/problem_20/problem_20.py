"""
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Usage:
    problem_19.py <max_number> [options]

Options:
    -h --help      Shows this screen.
    --test         Use "test" triangle
"""
from docopt import docopt
import operator


def product(list_of_numbers):
    return reduce(operator.mul, list_of_numbers, 1)


def run(max_number):
    answer = list([x for x in xrange(1, max_number + 1)])
    answer = product(answer)
    answer = sum([int(x) for x in str(answer)])
    return answer


if __name__ == '__main__':
    args = docopt(__doc__)
    answer = run(int(args['<max_number>']))
    print "Answer: %s" % answer
