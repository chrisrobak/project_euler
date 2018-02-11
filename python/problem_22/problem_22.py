"""
Using p022_names.txt 46K text file containing over
five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

Usage:
    problem_22.py [options]

Options:
    -h --help               Shows this screen.
    -f --file=<file>        FileName to parse
"""
from docopt import docopt
import os
from nomtropolis.utils.translations import a1z26_upper_alpha_to_num


def get_namescore(name):
    """
    Provided name, get namescore

    :param name: The name to process
    :type name: str()
    :returns: The namescore of the name
    :rtype: int()
    """
    namescore = 0
    for char in name:
        namescore += a1z26_upper_alpha_to_num.get(char)
    return namescore


def run(filename):
    """
    Provided a file of firstnames, find the total word scores of all names.

    :param filename: File filename/path of the file to process
    :type filename: str()
    :returns: Sum of all namescores in the file
    :rtype: int()
    """
    answer = 0
    if not os.path.isfile(filename):
        raise ValueError("{} doesn't exist".format(filename))
    with open(filename, 'rb') as infile:
        position = 1
        for line in infile:
            names = line.split(',')
            names = [x[1:-1] for x in names]
            names.sort()
            for name in names:
                namescore = get_namescore(name)
                answer += (namescore * position)
                position += 1
    return answer


if __name__ == '__main__':
    args = docopt(__doc__)
    filename = 'p022_names.txt'
    if args['--file']:
        filename = args['--file']
    answer = run(filename)
    print("Answer: {}".format(answer))
