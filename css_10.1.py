#Set 10.01

#There is a text file “jytky.txt” which contains some tweets from Finnish elections. Each tweet is on its own line. How many tweets there are in total in this file? Remove lines that are empty.

#Start with code:

#for line in open('jytky.txt‘).readlines():
#   print line

jytky = open('jytky.txt').readlines()
twiitit = 0
tyhjat = 0


for j in jytky:
	if j == "\n":
   		tyhjat = tyhjat + 1
   	else:
   		twiitit = twiitit + 1

print twiitit 