#Set 11.04

#From the file “jytky.txt” collect all tweet (texts) mentioning a user to a dictionary. The dictionary key is the username and the dictionary value is the list of the tweet texts; i.e.

#{ “user1” : [ “Tweet 1 text @user1”, “Tweet 2 text @user1 @user2” ], “user2” : [“Tweet 2 @user1 @user2”, “Tweet 3 @user2” ] }


import json
import re, string
import codecs
import io, json
import sys
import pickle

reload(sys)  
sys.setdefaultencoding('utf8')

jytky = open('jytky.txt').readlines()

users_mentions = {}
username = ''

#trying different versions of compliling
# pattern = re.compile('[\W_]+', re.UNICODE)
pattern = re.compile('[\W_]+')

for line in jytky:
	# if 'RT' not in line[:2]: #this line only if you want to skip retweets
	words_in_line = line.split()
	for x in words_in_line:
		if len(x)>1 and '@' in x:
			username = '@' + pattern.sub('', x)

			if username in users_mentions:
				users_mentions[username].append(line)
			else:
				users_mentions.setdefault(username, [])
				users_mentions[username].append(line)

#save as pickle-file for easier processing in next assignment
with open('jytky_mentions.pickle', 'wb') as f: 
    pickle.dump(users_mentions, f, pickle.HIGHEST_PROTOCOL)

#save into json to look at file and assess success
json.dump(users_mentions, open("jytky_mentions.json",'w'), indent=4, sort_keys=True, ensure_ascii=False)

