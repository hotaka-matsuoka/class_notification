import datetime
import time
import locale
# locale.setlocale(locale.LC_TIME, '')

dt_now = datetime.datetime.now()
year = dt_now.year
month = dt_now.month
day = dt_now.day
day_of_week = datetime.date(year, month, day).strftime('%a')