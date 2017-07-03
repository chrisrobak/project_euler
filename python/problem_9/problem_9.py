"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.




Usage:
    problem_9.py <target_number> [options]

Options:
    -h --help        shows this screen.
"""
import math
from docopt import docopt


def run(target_number):
    for b in xrange(2, target_number+1):
        for a in xrange(1, b):
            c = math.sqrt((a * a) + (b * b))
            if (a + b + c) == target_number:
                return a * b * c


if __name__ == '__main__':
    args = docopt(__doc__)
    target_number = int(args['<target_number>'])
    answer = run(target_number)
    print "Answer: %d" % answer
