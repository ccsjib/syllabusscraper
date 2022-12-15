from subprocess import call

call(['python', '!test.py'])
print("running")
call(['python', '!extract.py'])
print("ruinning2")