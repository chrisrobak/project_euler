"""
By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                        75
                      95 64
                     17 47 82
                    18 35 87 10
                  20 04 82 47 65
                 19 01 23 75 03 34
               88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
           41 48 72 33 47 32 37 16 94 29
         53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
   04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this
problem by trying every route. However, Problem 67, is the same
challenge with a triangle containing one-hundred rows!
it cannot be solved by brute force, and requires a clever method!

Usage:
    problem_18.py [options]

Options:
    -h --help      Shows this screen.
    --test         Use "test" triangle
"""
from docopt import docopt


def build_test_triangle():
    return [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3]
    ]


def build_triangle():
    return [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]


def get_best_path(rows, row_number):
    col_number = 0
    for column in rows[row_number]:
        rows[row_number][col_number] = max(
            rows[row_number+1][col_number] + rows[row_number][col_number],
            rows[row_number+1][col_number+1] + rows[row_number][col_number],
        )
        col_number += 1
    if row_number == 1:
        return sum(rows[0], max(rows[1][0], rows[1][1]))
    else:
        return get_best_path(rows, row_number - 1)


if __name__ == '__main__':
    args = docopt(__doc__)
    if args['--test']:
        triangle = build_test_triangle()
    else:
        triangle = build_triangle()
    answer = get_best_path(triangle, len(triangle) - 2)
    print "Answer: %d" % answer
