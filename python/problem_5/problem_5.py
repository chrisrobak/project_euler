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
    """
    Provided a number, find the smallest number such that every number
    number under <max_num> divides evenly into it. Basicall you find a
    number that 2 numbers divide equally into, add that number to itself
    until a 3rd number divides into it, then add it to itself again until
    a 4th does the same.. etc.. until you've used all the numbers.

    :param max_num: The largest number that needs to be a factor
    :type max_num: int()
    :returns: A number that all numbers under <max_num> can divide equally into
    :rtype: int()
    """
    current_number = max_num
    while current_number > 1:
        next_num = max_num
        while (max_num % current_number != 0):
            max_num += next_num
        current_number = current_number - 1
    return max_num


if __name__ == '__main__':
    args = docopt(__doc__)
    max_num = int(args['<max_number>'])
    print("Smallest multiple for: {}".format([x for x in range(1, max_num + 1)]))
    smallest_multiple = get_smallest_multiple_for_factorial(max_num)
    print("Smallest multiple: {}".format(smallest_multiple))
