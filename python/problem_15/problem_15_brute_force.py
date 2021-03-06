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


found_paths = 0
known_paths = []


def lattice_path(grid_size, x=0, y=0, paths_history=[]):
    """
    Brute force a lattice gride only going right + down

    :param grid_size: How big of a grid to navigate
    :type grid_size: int()
    :param x: x location on the grid
    :type x: int()
    :param y: y location on the grid
    :type y: int()
    :param paths_history: choices made so far
    :type paths_history: list()
    :returns: None
    :rtype: None
    """
    global found_paths
    global known_paths
    if len(paths_history) > 0:
        if paths_history[-1] == (x, y):
            return
    paths_history = paths_history[:]
    paths_history.append((x, y))
    while True:
        if x < grid_size:
            lattice_path(
                grid_size, x+1, y, paths_history
            )
        if y < grid_size:
            lattice_path(
                grid_size, x, y+1, paths_history
            )
        if x == grid_size and y == grid_size:
            # reached end
            if paths_history not in known_paths:
                known_paths.append(paths_history)
                found_paths += 1
            break
        else:
            break
    return found_paths


def run(grid_size):
    return lattice_path(grid_size)


if __name__ == '__main__':
    args = docopt(__doc__)
    run(int(args['<grid_size>']))
    print("Answer: {}".format(found_paths))
