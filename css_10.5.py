#Set 10.05

#File jytky_verkko.txt includes links on who tweeted to whom:

#1620879505 -> 125463318
#527224088 -> -
#584610998 -> -
#138152865 -> 283159564
#User 1620879505 has mentioned user 125463318, whereas user 527224088 has not mentioned anyone

#How many tweets are not directed to anyone?
#Who is the most active tweeter (sends out most tweets) Use dictionary here; do not use pre-made functions such as counter.


from collections import defaultdict

jytky = open('jytky_verkko.txt').readlines()

def directed_tweets(jytky):
	directed_count = 0
	undirected_count = 0

	for j in jytky:
		if "-> -" in j:
			undirected_count = undirected_count + 1
		else:
			directed_count = directed_count + 1

	print undirected_count

directed_tweets(jytky)

def amount_of_tweets(jytky):
	tweets_per_id = {}

	for j in jytky:
		id = j.split("->")[0]
		if id in tweets_per_id:
			tweets_per_id[id] += 1
		else:
			tweets_per_id[id] = 1

	return tweets_per_id

def most_tweets(jytky):
	most_active = ""
	their_tweets = 0
	to_loop = amount_of_tweets(jytky)

	for key in to_loop:
		if to_loop[key] > their_tweets:
			most_active = key
			their_tweets = to_loop[key]

	print "The most active tweeter is " + most_active + " with " + str(their_tweets) + " tweets"

most_tweets(jytky)


