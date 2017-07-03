"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is:

9009 (91 x 99)

Find the largest palindrome made from the product of two 3-digit numbers.

Usage:
    problem_4.py <num_digits> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt


def is_palindrome(num):
    num = str(num)
    start_count = 0
    while start_count < len(num) - 1:
        left_side = int(num[start_count:start_count+1])
        right_index_left = (start_count*-1)-1
        if right_index_left + 1 == 0:
            right_side = int(num[right_index_left:])
        else:
            right_side = int(num[right_index_left: right_index_left + 1])
        if left_side != right_side:
            return False
        start_count += 1
    return True


def get_max_palindrome_by_num_digits(num_digits):
    max_product = 0
    max_digit = int("9" * num_digits)
    next_digit = max_digit
    while max_digit > 0:
        while next_digit > 0:
            product = max_digit * next_digit
            if is_palindrome(product):
                if product > max_product:
                    max_product = product
            next_digit = next_digit - 1
        max_digit = max_digit - 1
        next_digit = max_digit
    return max_product


if __name__ == '__main__':
    args = docopt(__doc__)
    num_digits = int(args['<num_digits>'])
    max_palindrome = get_max_palindrome_by_num_digits(num_digits)
    print "Max Palindrome: %s" % str(max_palindrome)
