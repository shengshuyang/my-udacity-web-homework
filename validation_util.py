import cgi
import os

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


def valid_month(month):
    if month.title() in months:
        return month.title()
    return None


def valid_day(day):
    if not day.isdigit():
        return None
    day = int(day)
    if day > 0 and day <= 31:
        return day
    return None


def valid_year(year):
    if not year.isdigit():
        return None
    year = int(year)
    if year <= 2020 and year >= 1900:
        return year
    return None


def get_html(path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    index_path = dir_path + path
    return open(index_path).read()


def escape_html(s):
    if type(s) is not str:
        s = str(s)
    return cgi.escape(s, quote = True).encode('ascii', 'ignore')