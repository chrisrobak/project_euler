"""
If the numbers 1 to 5 are written out in words:

one, two, three, four, five

Then there are

3 + 3 + 5 + 4 + 4 = 19

letters used in total.

If all the numbers from 1 to 1000 inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters,
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance
with British usage.

Usage:
    problem_17.py <max_num> [options]

Options:
    -h --help        shows this screen.
"""
from docopt import docopt


lookup = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety'
}


def three_digit_to_word(num):
    """
    Convert a three digit number to a word.

    :param num: The number to convert
    :type num: int()
    :returns: A string describing the number
    :rtype: str()
    """
    if num % 100 == 0:
        return "%s hundred" % lookup[int(str(num)[0])]
    else:
        num = str(num)
        first = int(num[0])
        second = int(num[1:])
        return "%s hundred and %s" % (
            lookup[first],
            lookup.get(second, two_digit_to_word(second))
        )


def two_digit_to_word(num):
    """
    Convert a two digit number to a word

    :param num: The number to convert
    :type num: int()
    :returns: A string describing the number
    :rtype: str()
    """
    if num in lookup:
        return num
    return "%s-%s" % (
        lookup[int(str(num)[0]+'0')],
        lookup[int(str(num)[1])]
    )


def number_to_word(num):
    """
    Aggregate method, based on how large number is,
    call specific function to format the number.

    :param num: The number to convert
    :type num: int()
    :returns: A string describing the number
    :rtype: str()
    """
    if num in lookup:
        return lookup[num]
    elif num < 100:
        return two_digit_to_word(num)
    elif num < 1000:
        return three_digit_to_word(num)
    elif num == 1000:
        return 'one thousand'
    else:
        raise ValueError('Too large of number!: %s' % num)


def run(max_num):
    """
    For each number under <max_num> add the number of letters
    together to get the answer

    :param max_num: The maximum number to start with
    :type max_num: int()
    :returns: The number of letters in all words under <max_num>
    :rtype: int()
    """
    answer = 0
    for x in range(1, max_num + 1):
        word = number_to_word(x)
        word = word.replace(' ', '').replace('-', '')
        num_letters = len(word)
        answer += num_letters
    return answer


if __name__ == '__main__':
    args = docopt(__doc__)
    answer = run(int(args['<max_num>']))
    print("Answer: {}".format(answer))
