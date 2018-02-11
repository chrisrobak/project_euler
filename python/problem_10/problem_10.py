"""
note* the nomtropolis librar is my personal repo
will rename + make public soon.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Usage:
    problem_10.py <max_number> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt
from nomtropolis.utils.digits import primes


def run(max_number):
    """
    Get the sum of all primes below a number

    :param max_number: The number of which no prime should exceed
    :type max_number: int()
    ;returns: The sum of primes
    :rtype: int()
    """
    answer = 0
    for prime in primes.generate_up_to(max_number):
        answer += prime
    return answer


if __name__ == '__main__':
    args = docopt(__doc__)
    print("Answer: %d" % run(int(args['<max_number>'])))
