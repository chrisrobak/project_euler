"""
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Usage:
    problem_19.py <max_number> [options]

Options:
    -h --help      Shows this screen.
"""
from docopt import docopt
from functools import reduce
import operator


def product(list_of_numbers):
    """
    Multiply all numbers in a list together

    :param list_of_numbers: A list of numbers
    :type list_of_numbers: list()
    :returns The product of all numbers in the list
    :rtype: int()
    """
    return reduce(operator.mul, list_of_numbers, 1)


def run(max_number):
    """
    Multiple every number up to <max_number>
    Then add the numbers of the product

    :param max_number: The max number to include
    :type max_number: int()
    :returns: The sum of the digits of the product
    :rtype: int()
    """
    answer = list([x for x in range(1, max_number + 1)])
    answer = product(answer)
    answer = sum([int(x) for x in str(answer)])
    return answer


if __name__ == '__main__':
    args = docopt(__doc__)
    answer = run(int(args['<max_number>']))
    print("Answer: {}".format(answer))
