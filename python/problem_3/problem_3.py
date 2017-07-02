"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Usage:
    problem_3.py <max_number> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt


def _is_prime(number, known_primes):
    for prime_number in known_primes:
        if number % prime_number == 0:
            return False
    return True


def _prime_factorize(num, factors, known_primes, possible_factor):
    if num % possible_factor == 0:
        factors.append(possible_factor)
        num = num / possible_factor
        factor_index = 0
        for prime in known_primes:
            _prime_factorize(num, factors[factor_index:], known_primes, prime)
            factor_index += 1
    return num, factors


def get_prime_factors(target_number):
    primes = []
    current_number = 3
    target_number, prime_factors = _prime_factorize(
        target_number, [], primes, 2)
    while True:
        # print 'current_number: %s,\nknown_primes: %s,\nfactors: %s' % (
        #     current_number,
        #     primes,
        #     prime_factors
        # )
        if _is_prime(current_number, primes):
            primes.append(current_number)
            target_number, prime_factors = _prime_factorize(
                target_number, prime_factors, primes, current_number)
        current_number += 2
        if target_number == 1:
            break
        elif target_number in primes:
            prime_factors.append(target_number)
            break
    return prime_factors

if __name__ == '__main__':
    args = docopt(__doc__)
    target_number = int(args['<max_number>'])
    prime_factors = get_prime_factors(target_number)
    print "Prime Factors: %s" % ', '.join([str(x) for x in prime_factors])
    print "Max Prime Factor: %d" % max(prime_factors)
