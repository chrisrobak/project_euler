"""
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the
proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though
it is known that the greatest number that cannot be expressed as the sum
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.

Usage:
    problem_23.py [options]

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
