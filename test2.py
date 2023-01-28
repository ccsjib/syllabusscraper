from datetime import date, timedelta


day = date.today()
weekNum = day.weekday()



print(day)

#.strftime("%#d")

while weekNum >= 5:
    day -= timedelta(days=1)
    weekNum -= 1
    print(weekNum)
    print(day)

dayNum = int(day.strftime("%#d"))

#dayNum = int(day)
print(dayNum)