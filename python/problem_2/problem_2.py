"""
Each new term in the Fibonacci sequence is generated by adding
the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.

Usage:
    problem_2.py <max_number> [options]

Options:
    -h --help      Shows this screen.
"""
from docopt import docopt


def problem2(max_number):
    """
    Sum of even valued fibonacci under <max_number>

    :param max_number: The max fibonacci value to consider
    :type max_number: int()
    :returns: The sum of the even valued fibonacci numbers
    :rtype: int()
    """
    answer = 0
    fib_value = 1
    current_number = 1
    previous_number = 1
    while fib_value < max_number:
        fib_value = current_number
        if fib_value >= max_number:
            return answer
        if fib_value % 2 == 0:
            answer += current_number
        current_number += previous_number
        previous_number = current_number-previous_number


if __name__ == '__main__':
    args = docopt(__doc__)
    print(problem2(int(args['<max_number>'])))
