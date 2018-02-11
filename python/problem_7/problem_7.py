"""
note* nomtropolis library is my personal repo,
will rename + make it public soon

By listing the first six prime numbers:

2, 3, 5, 7, 11, 13

we can see that the 6th prime is 13.

What is the 10001st prime number?

Usage:
    problem_7.py <nth_prime> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt
from nomtropolis.utils.digits import primes


def run(nth_prime):
    """
    Provided a number n, find the nth prime.

    :param nth_prime: The number in the sequence of primes
    :type nth_prime: int()
    :returns: The nth prime
    :rtype: int()
    """
    num_found = 0
    for prime in primes.generate():
        num_found += 1
        if num_found == nth_prime:
            return prime


if __name__ == '__main__':
    args = docopt(__doc__)
    max_num = int(args['<nth_prime>'])
    answer = run(max_num)
    print("Answer: %d" % answer)
