import os
import json
import re
from datetime import date



#print(datetime.datetime(2015, 3, 5).strftime('%#d'))

today = date.today()

dayNum = today.strftime("%#d")
print(dayNum)