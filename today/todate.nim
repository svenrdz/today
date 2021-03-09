import times
import strutils

type
  Todate = ref object
    year: int
    week: char
    day: int

proc `$`*(todate: Todate): string = $todate.year & $todate.week & $todate.day

func initTodate(year: int, week: char, day: int): Todate =
  Todate(year: year, week: week, day: day)

func toTodate*(todate: string): Todate =
  let year = todate[0..<2].parseInt
  let week = todate[2]
  let day = parseInt($todate[3])
  initTodate(year, week, day)

func toTodate*(dt: Datetime): Todate =
  var yearday = dt.yearday + 1 # 1st Jan has yearday 0
  if yearday > 60 and dt.year.isLeapYear:
    dec yearday
  let weekInt = yearday div 10
  let week =
    if weekInt < 10:
      weekInt.`$`[0]
    else:
      char('a'.ord + weekInt - 10)
  initTodate(dt.year mod 100, week, yearday mod 10)

func toInt(week: char): int =
  try: parseInt($week)
  except: week.ord - 'a'.ord + 10

func yearday(todate: Todate): int =
  result = 10 * todate.week.toInt + todate.day
  if result > 59 and todate.year.isLeapYear: inc result

proc toDatetime*(todate: Todate): Datetime =
  initDatetime(31, mDec, todate.year + 1999, 00, 00, 00) + initDuration(
      days = todate.yearday)

# TODO: handle last 5 days of the year
