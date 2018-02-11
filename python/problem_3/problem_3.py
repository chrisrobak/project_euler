"""
note: nomtropolis library is my private repo but will make public/rename it soon.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Usage:
    problem_3.py <max_number> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt
from nomtropolis.utils.digits import primes


def get_prime_factors(target_number, prime_factors=[]):
    """
    Privided a number, get all prime factors for it.

    :param target_number: The number to get prime factors for
    :type target_number: int()
    :returns: A list of prime factors (int) of <target_number>
    :rtype: list()
    """
    if primes.is_prime(target_number):
        prime_factors.append(int(target_number))
        return prime_factors
    if target_number == 1:
        return prime_factors
    for prime in primes.generate():
        print("Checking prime: {}".format(prime))
        if target_number % prime == 0:
            prime_factors.append(prime)
            target_number = target_number / prime
            return get_prime_factors(target_number, prime_factors)


if __name__ == '__main__':
    args = docopt(__doc__)
    target_number = int(args['<max_number>'])
    prime_factors = get_prime_factors(target_number)
    print("Prime Factors: %s" % ', '.join([str(x) for x in prime_factors]))
    print("Max Prime Factor: %d" % max(prime_factors))
