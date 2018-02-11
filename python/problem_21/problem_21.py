"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are:
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110
therefore d(220) = 284.
The proper divisors of 284 are:
1, 2, 4, 71 and 142
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Usage:
    problem_21.py <max_number> [options]

Options:
    -h --help      Shows this screen.
"""
from docopt import docopt


def proper_divisors(number):
    """
    Yield out proper divisors of a number

    :param number: The number to get proper divisors for
    :type number: int()
    :returns: This is a generator, yields integers
    :rtype: iterable
    """
    yield 1
    number = int(number)
    for i in range(2, number//2 + 1):
        if number % i == 0:
            yield i


def run(max_number):
    """
    Provided a number, find sum of all amicable pairs below.

    :param max_number: Largest number of an amicable pair
    :type max_number: int()
    :returns: Sum of all amicable pairs under provided number
    :rtype: int()
    """
    answer = 0
    for x in range(4, max_number):
        divisor_sum = sum(proper_divisors(x))
        if divisor_sum == x:
            continue
        divisor_sum_of_divisor_sum = sum(
            proper_divisors(divisor_sum)
        )
        if divisor_sum_of_divisor_sum == x:
            answer += x
    return answer


if __name__ == '__main__':
    args = docopt(__doc__)
    answer = run(int(args['<max_number>']))
    print("Answer: {}".format(answer))
