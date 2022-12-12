import os
import json
import re
from datetime import date

today = date.today()

dategoogle = today.strftime("%b %#d")

print(dategoogle)

with open("psychsyllabus.json", "r") as f:
    data = json.load(f)
 
test = "Prepare for Progress Check #8\nExit Ticket Questions ( Mod. 31 and 32 Optional) \n"   
    
if test in data:
    print("fopund it ")
else: 
    print("failed")
        