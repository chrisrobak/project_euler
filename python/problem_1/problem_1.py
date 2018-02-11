"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Usage:
    problem_1.py <max_number> [options]

Options:
    -h --help         shows this screen
"""
from docopt import docopt


def problem_1(max_number):
    """
    Sum of all multiples of 3 or 5 below <max_number>

    :param max_number: Max number to calculate
    :type max_number: int()
    :returns: Sum of all multiples of 3 or 5 below <max_number>
    :rtype: int()
    """
    answer = 0
    for x in range(1, max_number):
        if x % 3 == 0 or x % 5 == 0:
            answer += x
    return answer


if __name__ == '__main__':
    args = docopt(__doc__)
    print(problem_1(int(args['<max_number>'])))
