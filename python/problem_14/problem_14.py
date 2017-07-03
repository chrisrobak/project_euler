"""
The following iterative sequence is defined for the set
of positive integers:

divide by 2 if n is even
multiply by 3 then + 1 if n is odd

Using the rules above and starting with 13, we generate
the following sequence:
13, 40, 20, 10, 5, 16, 8, 4, 2, 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Usage:
    problem_14.py <max_chain_start> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt


def build_collatz_chain(number):
    chain = []
    if number == 1:
        return [1]
    while True:
        chain.append(number)
        if number % 2 == 0:
            number = number / 2
        else:
            number = (3 * number) + 1
        if number == 1:
            chain.append(number)
            return chain


def run(max_num):
    longest_chain = 0
    while max_num > 0:
        chain = build_collatz_chain(max_num)
        chain_size = len(chain)
        # print "%s has %s chain" % (
        #     max_num,
        #     chain_size
        # )
        if chain_size > longest_chain:
            print "%s has longest chain so far: %s long" % (
                max_num,
                chain_size
            )
            longest_chain = chain_size
        max_num = max_num - 1
    return longest_chain


if __name__ == '__main__':
    args = docopt(__doc__)
    print "Answer: %d" % run(int(args['<max_chain_start>']))
