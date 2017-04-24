#Set 10.03

#Search from the “jytky.txt” file all Tweets which include the word “RT” (i.e. it seems they are retweeted) and write those into file “jytky_myname.txt”

jytky = open('jytky.txt').readlines()
f = open('jytky_myname.txt', 'w+')

for j in jytky:
	if "RT" in j:
   		f.write(j)
   	
