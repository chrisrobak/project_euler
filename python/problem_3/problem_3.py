"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Usage:
    problem_3.py <max_number> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt


def prime_factorize(target_number):
    known_primes = []
    prime_factors = []
    current_number = 2
    while True:
        is_prime = 1
        for prime_number in known_primes:
            if current_number % prime_number == 0:
                is_prime = 0
        if is_prime:
            known_primes.append(current_number)
            if target_number % current_number == 0:
                prime_factors.append(current_number)
                target_number = target_number / current_number
                for prime_number in known_primes:
                    if target_number % prime_number == 0:
                        prime_factors.append(prime_number)
                        target_number = target_number / prime_number
        current_number += 1
        if target_number == 1 or target_number in known_primes:
            break
    return prime_factors

if __name__ == '__main__':
    args = docopt(__doc__)
    target_number = int(args['<max_number>'])
    prime_factors = prime_factorize(target_number)
    print "Prime Factors: %s" % ', '.join([str(x) for x in prime_factors])
    print "Max Prime Factor: %d" % max(prime_factors)
