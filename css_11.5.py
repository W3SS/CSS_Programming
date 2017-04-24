#Set 11.05

#Based on dictionary developed on the previous exercise, compute how many times each user is mentioned in a tweet which contains a reference to a) Helsingin Sanomat / HS, b) YLE, c) Iltasanomat or d) Iltalehti (names of Finnish newspapers). 
#Print each username and the number of tweets next to it.

import pickle

with open('jytky_mentions.pickle', 'rb') as handle:
    b = pickle.load(handle)

mentions = {}

for key in b:
	mentions[key] = 0
	for v in b[key]:
		if "Helsingin Sanomat" in v:
			mentions[key]+=1
		if "HS" in v:
			mentions[key]+=1
		if "Yle" in v:
			mentions[key]+=1
		if "Iltasanomat" in v:
			mentions[key]+=1
		if "Iltalehti" in v:
			mentions[key]+=1

print mentions