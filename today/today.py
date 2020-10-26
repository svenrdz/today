#!/usr/bin/env python
import sys
import datetime


def bisextile(year):
    return year % 4 == 0


def convert(date_or_year, month=None, day=None):
    if all(isinstance(x, (int, float)) for x in [date_or_year, month, day]):
        date = datetime.datetime(date_or_year, month, day)
    else:
        date = date_or_year
    days = date - datetime.datetime(date.year - 1, 12, 31)
    if days.days > 60 and bisextile(date.year):
        days -= datetime.timedelta(days=1)
    month = days.days // 10
    if month >= 10:
        month = chr(ord("a") + month - 10)
    day = days.days % 10
    return "".join(map(str, [date.year % 100, month, day]))


def revert(todate: str):
    assert isinstance(todate, str)
    todate = todate.strip()
    assert len(todate) == 4
    year = int(todate[:2]) + 2000
    try:
        tens = int(todate[2])
    except ValueError:
        tens = ord(todate[2]) - ord("a") + 10
    days = 10 * tens + int(todate[3])
    if days > 59 and bisextile(year):
        days += 1
    date = datetime.datetime(year - 1, 12, 31) + datetime.timedelta(days=days)
    return date.strftime("%d, %b %Y")


def today():
    print(convert(datetime.datetime.today()))


def dateof():
    print(revert(sys.argv[1]))
