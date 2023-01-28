from datetime import date, timedelta


today = date.today().weekday()

while today >= 5:
    today -= 1
  
print(today)
print(date.today())