"""
You are given the following information, but you may prefer to do some research

- 1900-01-01 was a Monday.
- Thirty days hath September,
  April, June and November.
  when short february's done (28, 29 on leap year)
  all the rest have 31
- A leap year occurs on any year evenly divisible by 4,
  but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month
during the twentieth century (1901-01-01 to 2000-12-31)?

Usage:
    problem_19.py [options]

Options:
    -h --help      Shows this screen.
    --test         Use "test" triangle
"""
from docopt import docopt


class Year(object):
    days = {
        0: 'sunday',
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday'
    }

    def __init__(self, year_number):
        self.year_number = year_number

    @staticmethod
    def _get_month_by_name(month):
        month = str(month).lower().replace('.', '')
        if month in ('jan', 'january'):
            return 0
        elif month in ('feb', 'february'):
            return 1
        elif month in ('mar', 'march'):
            return 2
        elif month in ('apr', 'april'):
            return 3
        elif month in ('may',):
            return 4
        elif month in ('jun', 'june'):
            return 5
        elif month in ('jul', 'july'):
            return 6
        elif month in ('aug', 'august'):
            return 7
        elif month in ('sep', 'september'):
            return 8
        elif month in ('oct', 'october'):
            return 9
        elif month in ('nov', 'november'):
            return 10
        elif month in ('dec', 'december'):
            return 11
        raise ValueError('Month :%s now known!' % month)

    @staticmethod
    def _days_in_month(month, leap_year=0):
        if isinstance(month, basestring):
            month_num = Year._get_month_by_name(month)
        else:
            month_num = int(month)
        if month_num == 1:
            if leap_year:
                return 28
            return 27
        elif month_num in (8, 3, 5, 10):
            return 29
        else:
            return 30

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
            else:
                return True
        return False

    @staticmethod
    def get_day_name_at_date(year, month, day):
        if isinstance(year, basestring):
            year = int(year)
        if year == 1900 and month == 0 and day == 0:
            return Year.days[1]
        else:
            # we know 1900-01-01 was a monday
            known_year = 1900
            known_month = 0
            known_day_name = 1
            known_month_day = 0
            while True:
                is_leap_year = Year.is_leap_year(known_year)
                while True:
                    while known_month_day <= Year._days_in_month(known_month, is_leap_year):
                        if known_year == year \
                           and known_month == month \
                           and known_month_day == day:
                            return Year.days[known_day_name]
                        if known_day_name == 6:
                            known_day_name = 0
                        else:
                            known_day_name += 1
                        known_month_day += 1
                    known_month_day = 0
                    known_month += 1
                    if known_month == 12:
                        known_month = 0
                        break
                known_year += 1


def run():
    year = 1901
    month = 0
    day = 0
    num_sunday_first_day_of_month = 0
    while True:
        print "on: %s-%s-%s" % (year, month, day)
        if day == 0:
            day_of_week = Year.get_day_name_at_date(year, month, day)
            print "first of month is: %s" % day_of_week
            if day_of_week == 'sunday':
                num_sunday_first_day_of_month += 1
        if year == 2000:
            if month == 11:
                if day == 30:
                    break
        if Year._days_in_month(month) == day:
            print 'here'
            day = 0
            if month == 11:
                year += 1
                month = 0
            else:
                month += 1
        else:
            day += 1
    return num_sunday_first_day_of_month


if __name__ == '__main__':
    args = docopt(__doc__)
    answer = run()
    print "Answer: %s" % answer
