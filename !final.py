from subprocess import call


#This first runs the retrieval API file and then the homework extraction file.
#I kept these files separate because I thought !retrieve would need to run less times per day than !extract.
#But I just realized they need to run together, so in my next version I will combine the files or simplify the code to not require a 3rd file.
call(['python', '!retrieve.py'])
print("retrieving")
call(['python', '!extract.py'])
print("extracting homework data")


#if the authentication issue happens: sign out first https://stackoverflow.com/questions/65821740/google-api-oauth-2-sign-in-something-went-wrong-with-new-oauth-2-client