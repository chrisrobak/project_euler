"""


Usage:
    problem_24.py [options]

Options:
    -h --help               Shows this screen.
"""
from docopt import docopt
from itertools import product


def get_proper_divisors(number):
    """
    Get proper dvisors for a number

    :param number: The number to get divisors for
    :type number: int()
    :returns: A list of divisors
    :rtype: list()
    """
    divisors = []
    for i in range(1, number//2 + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def generate_abundant_numbers(limit=28123):
    """
    Generate abundant numbers up to limit

    :param limit: Only generate up to this
    :type limit: int()
    :returns: Is a generator, yields integers
    :rtype: iterable
    """
    number = 1
    while True:
        divisors = get_proper_divisors(number)
        if number > limit:
            break
        if sum(divisors) > number:
            yield number
        number += 1


def run():
    """
    Generates abundant numbers
    generates cartesian product of all abundant_numbers
    filters a range down from what doesn't exist

    :returns: Sum of all numbers not created by abundant numbers
    :rtype: int()
    """
    abundant_numbers = set(generate_abundant_numbers())
    made_from_abundant_numbers = set(map(
        sum,
        product(abundant_numbers, repeat=2)
    ))
    uncreated_numbers = set(range(1, 28124)) - made_from_abundant_numbers
    answer = sum(uncreated_numbers)
    return answer


if __name__ == '__main__':
    args = docopt(__doc__)
    answer = run()
    print("Answer: {} should be: {}, difference of {}".format(
        answer,
        4179871,
        abs(answer - 4179871)
    ))
