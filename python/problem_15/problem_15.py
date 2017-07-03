"""
Starting in the top left corner of a 2x2 grid, and only being able
to move to the right and down, there are exactly 6 routes to the
bottom right corner.

How many such routes are there through a 20x20 grid?

Usage:
    problem_15.py <grid_size> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt


def lattice_path(grid_size):
    y = 0
    matrix = {}
    while y <= grid_size:
        x = 0
        while x <= grid_size:
            if x == 0 or y == 0:
                matrix[(x, y)] = 1
            elif x > 0:
                if y > 0:
                    matrix[(x, y)] = matrix[(x - 1, y)] + matrix[x, y - 1]
            x += 1
        y += 1
    return matrix[grid_size, grid_size]


def run(grid_size):
    return lattice_path(grid_size)


if __name__ == '__main__':
    args = docopt(__doc__)
    answer = run(int(args['<grid_size>']))
    print "Answer: %d" % answer
