"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Usage:
    problem_3.py <max_number> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt
from nomtropolis.numbers.primes import Primes


def get_prime_factors(target_number, prime_factors=[]):
    prime_factors = prime_factors
    for prime in Primes.generate_primes():
        if target_number % prime == 0:
            prime_factors.append(prime)
            target_number = target_number / prime
        if Primes.is_prime(target_number):
            prime_factors.append(target_number)
            break
        if target_number == 1:
            break
    return prime_factors

if __name__ == '__main__':
    args = docopt(__doc__)
    target_number = int(args['<max_number>'])
    prime_factors = get_prime_factors(target_number)
    print "Prime Factors: %s" % ', '.join([str(x) for x in prime_factors])
    print "Max Prime Factor: %d" % max(prime_factors)
