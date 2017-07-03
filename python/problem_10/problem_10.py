"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Usage:
    problem_10.py <max_number> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt
from nomtropolis.numbers.primes import Primes


def run(max_number):
    answer = 0
    for prime in Primes.generate_primes(max_number):
        answer += prime
    return answer

if __name__ == '__main__':
    args = docopt(__doc__)
    print "Answer: %d" % run(int(args['<max_number>']))
