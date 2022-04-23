from datetime import date, datetime, timedelta
import time

# today
today = date.today()
print(today)
print(today.day)

# now
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.second)

# # custom date & time
# print(date(2022, 3, 12))
# print(time(4, 32, 34))

# # format
# print(now.strftime("%b %d, %Y - %H:%M:%S"))
# print(today.strftime('%d %b %Y'))


# # Countdown 
# hackathon_date = datetime(year=2022, month=5, day=6, hour=9)
# countdown = hackathon_date - datetime.now()
# print(f"Countdown to hackathon: {countdown.days} days, {countdown.seconds} seconds.")

# # Calculation
# now = datetime.now()
# print(now)
# tomorrow = timedelta(days=3)
# print(now+tomorrow)

# # Timer
# timer = 10
# def setInterval(timer):
#     while timer != -1:
#         print(timer)
#         time.sleep(1)
#         timer -= 1

# setInterval(timer)