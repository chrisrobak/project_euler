"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?


Usage:
    problem_16.py [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt


def run():
    number = str(2**1000)
    return sum([int(x) for x in number])


if __name__ == '__main__':
    args = docopt(__doc__)
    answer = run()
    print("Answer: {}".format(answer))
