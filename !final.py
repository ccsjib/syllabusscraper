from subprocess import call


#This first runs the retrieval API file and then the homework extraction file.
#I kept these files separate because I thought !retrieve would need to run less times per day than !extract.
#But I just realized they need to run together, so in my next version I will combine the files or simplify the code to not require a 3rd file.
call(['python', '!retrieve.py'])
print("running")
call(['python', '!extract.py'])
print("ruinning2")