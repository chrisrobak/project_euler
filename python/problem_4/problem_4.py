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
    """
    Check if a number is a palindrome

    :param num: The number to check
    :type num: int()
    :returns: Whether or not the number is a palindrome
    :rtype: bool()
    """
    return str(num) == str(num)[::-1]


def get_max_palindrome_by_num_digits(num_digits):
    """
    Provided number of digits, find largest palindrome number created
    by multiplying two numbers of x digits.

    :param num_digits: how 'big' a number should be ie - 2 = 99, 3 = 999
    :type num_digits: int()
    :returns: A palindromic product
    :rtype: int()
    """
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
    print("Max Palindrome: {}".format(max_palindrome))
