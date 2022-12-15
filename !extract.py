import os
import json
import re
from datetime import date

today = date.today()

day = today.strftime("%#d")
dayNum = int(day)

suffix = ""
if 4 <= dayNum <= 20 or 24 <= dayNum <= 30:
    suffix = "th"
else:
    suffix = ["st", "nd", "rd"][dayNum % 10 - 1]

#https://www.tutorialspoint.com/How-do-I-display-the-date-like-Aug-5th-using-python-s-strftime#:~:text=It%20is%20not%20possible%20to,directive%20that%20supports%20this%20formatting.
dategoogle = today.strftime("%b %#d" + suffix)


with open("psychsyllabus.json", "r") as f:
    data = json.load(f)
#https://linuxhint.com/search_json_python/ 
#print(data)
#I just realized that the JSON is formatted as a Py list so I can just use the search function of that. https://www.freecodecamp.org/news/python-find-in-list-how-to-find-the-index-of-an-item-or-element-in-a-list/





#data is already formatted as a Python list, so I can treat it as one rather than as a JSON.

#https://docs.python.org/3.4/tutorial/datastructures.html#list-comprehensions
#this code
#answer = []
#for strings in data:
#    if dategoogle + "  (F)" in strings or dategoogle + " (F)" in strings or dategoogle + " (D, F)" in strings:
#        answer.append(strings)
#print(answer)

#is simplified to


answer = [strings for strings in data if dategoogle + "  (F)" in strings or dategoogle + " (F)" in strings or dategoogle + " (D, F)" in strings or dategoogle + "  (B, D, F)" in strings or dategoogle + " \n(B, D, F)" in strings]

#ans = [x for x in answer if dategoogle and "F" in x]

#Finds what position my answer is in the list. Since homework is 2 strings past the date in the list, add 2
homeworkIndex = data.index(answer[0]) + 2
print(data[homeworkIndex])

with open('HOMEWORK.TXT', 'w') as f:
    f.write(dategoogle + '\n')
    f.write(data[homeworkIndex])


#data is already formatted as a Python list

#for value in jsondata:
    #if (jsondata[value] == dategoogle):
       # print("foundljkfhejrsltkfjhe")
    #else:
       # print("big fail")
        
