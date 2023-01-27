import os
import json
import re
from datetime import date

#gets date using datetime (already part of Python)
today = date.today()

day = today.strftime("%#d")
dayNum = int(day)

#Adds suffix to the date since AP Psych's syllabus has them. Makes sure string finding using matching works later.
suffix = ""
if 4 <= dayNum <= 20 or 24 <= dayNum <= 30:
    suffix = "th"
else:
    suffix = ["st", "nd", "rd"][dayNum % 10 - 1]

#https://www.tutorialspoint.com/How-do-I-display-the-date-like-Aug-5th-using-python-s-strftime#:~:text=It%20is%20not%20possible%20to,directive%20that%20supports%20this%20formatting.


#Date which will be used to match syllabus JSON.
dategoogle = today.strftime("%b %#d" + suffix)



#Open JSON file which has syllabus pulled from Google Docs API converted into a Python list (one string for each cell)
with open("psychsyllabus.json", "r") as f:
    data = json.load(f)
#https://linuxhint.com/search_json_python/ 
#print(data)
#(while coding) I just realized that the JSON is formatted as a Py list so I can just use the search function of that. https://www.freecodecamp.org/news/python-find-in-list-how-to-find-the-index-of-an-item-or-element-in-a-list/





#data is already formatted as a Python list, so I can treat it as one rather than as a JSON.

#https://docs.python.org/3.4/tutorial/datastructures.html#list-comprehensions
#this code
#answer = []
#for strings in data:
#    if dategoogle + "  (F)" in strings or dategoogle + " (F)" in strings or dategoogle + " (D, F)" in strings:
#        answer.append(strings)
#print(answer)

#is simplified to (answer var below)

#find any strings matching the date + all the different ways the teacher might have written F Block (I hope to find a better way to do this in my next version)
answer = [strings for strings in data if dategoogle + "  (F)" in strings or dategoogle + " (F)" in strings or dategoogle + " (D, F)" in strings or dategoogle + "  (B, D, F)" in strings or dategoogle + " \n(B, D, F)" in strings or dategoogle + " (B, D)" in strings]

#ans = [x for x in answer if dategoogle and "F" in x]

#Finds what position my answer is in the list. Since homework is 2 strings past the date in the list, add 2
homeworkIndex = data.index(answer[0]) + 2
print(data[homeworkIndex])

#opens a text file and puts the homework for the current day in there.
with open('HOMEWORK.TXT', 'w') as f:
    f.write(dategoogle + '\n')
    f.write(data[homeworkIndex])



