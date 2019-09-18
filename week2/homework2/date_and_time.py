from datetime import datetime
dt_now = datetime.now()
print(dt_now)

yesterday = datetime(2019, 9, 18)
print(yesterday)

month_ago = datetime(2019, 8, 18)
print(month_ago)

date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt)