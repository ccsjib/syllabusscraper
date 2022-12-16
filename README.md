# syllabusscraper


So, back in Freshman year I wanted my computer desktop to be cooler and I found this program called Rainmeter. It allows you to put various customized and interactive widgets on your desktop. It has its own scripting language, but as a beginner I downloaded others' published widgets to get the look I wanted. Eventually, I stumbled upon an interactive dock ([Interactive Dock](https://www.deviantart.com/not-finch/art/Interactive-Dock-for-Rainmeter-772713805)) which lets you open programs. I had gotten more comfortable with Rainmeter so I was able to understand how this widget worked. I changed the animation speed and orientation along with connecting each button to my class documents folders and giving them icons. 

![raimeter dock](https://github.com/ccsjib/syllabusscraper/blob/main/RainmeterDock.png)

It came out great, but then I had a crazy idea. I was really tired of checking class syllabi every day to know my homework. What if I wrote code that did it for me and displayed right next to the class block icon on this dock? And what if the class icons rearranged based on the day's schedule? 

And that's where this idea was born. Since the schedule-based icons were a lower priority, I decided to start with the syllabus info. Unfortunately I'm coming back to it 3 years later when there's not much time left to make use of it, but I would love to evolve this into something any Cannon student can use. It's still a long way from there, mainly because a reliable solution would include changing the format of teachers' syllabi to be uniform or to use a database, but it would be an amazing tool for all students to have. 

The original scope of this AT: C+CS project was to have a fully functional scraper that looked through all of my class syllabi and displayed when hovering over the class block icon on the Rainmeter dock. But as I continued working, I realized that this was not an achievable goal for me in the time we had, so I pivoted. I decided to focus on getting one syllabus (AP Psych) working and have it output somewhere other than the terminal, even if it was not Rainmeter-related. Since Rainmeter has its own scripting language, it would be like learning another coding language just to make a text box, and I was concerned I wouldn't have enough time for this (I was right lol).

The code starts with !retrieve.py. This is a modified version of the Google Docs API python quickstart file which has the required code to get the API to function. I modified it to:
- only use the code that accesses the table element (since AP Psych's syllabus has all the info in a table)
- append the contents of each cell as a string to a Python list
- send that list to psychsyllabus.JSON
I don't know that I necessarily need a JSON here, but I think it could make things easier if I decide to take advantage of the key:value setup.

In !extract.py, which I made from scratch, the code:
- finds the current day number in the month
- adds the current suffix (since the AP Psych syllabus uses them)
- searches the list in psychsyllabus.JSON for anything matching the date + different possible combinations of F Block (Could be (F), (B, F), (B, D, F), etc.)
- finds the position of this string in the list
- adds 2 because homework is two cells to the right of date
- sends that string to HOMEWORK.txt

HOMEWORK.txt is accessed by Rainmeter using a piece of a Raimeter widget (skin) I found online which reads a .txt since Rainmeter alone can't do this. I wanted to connect this to the dock, but unfortunately with the time constraints I did not think this was doable. Instead, I decided to learn very basic Rainmeter scripting and got some draggable text to display on my desktop!

Overall I'm really happy with this project. I wish I was able to do more in the time given, but it is a functional syllabus scraper! For my next version, I will be focusing on:
- the other syllabi
- dock integation
- code clean-up 

