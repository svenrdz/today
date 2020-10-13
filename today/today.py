#!/usr/bin/env python
import datetime


def convert(date_or_year, month=None, day=None):
    if all(isinstance(x, (int, float)) for x in [date_or_year, month, day]):
        date = datetime.datetime(date_or_year, month, day)
    else:
        date = date_or_year
    days = date - datetime.datetime(date.year - 1, 12, 31)
    month = days.days // 10
    if month >= 10:
        month = chr(ord("a") + month - 10)
    day = days.days % 10
    return "".join(map(str, [date.year % 100, month, day]))


def main():
    print(convert(datetime.datetime.today()))


if __name__ == "__main__":
    main()
