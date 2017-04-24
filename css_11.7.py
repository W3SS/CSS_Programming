#Set 11.07

#File jytky_verkko.txt includes links on who tweeted to whom:

#1620879505 -> 125463318
#527224088 -> -
#584610998 -> -
#138152865 -> 283159564
#User 1620879505 has mentioned user 125463318, whereas user 527224088 has not mentioned anyone.

#Who receives most tweets?
#Who sends out most tweets which do not mention others? 

#Use dictionary here; do not use pre-made functions such as counter.

jytky = open('jytky_verkko.txt').readlines()

receive_count = {}
senders = {}

for line in jytky:
	sender = line.partition(" ")[0]
	receiver = line.partition("-> ")[2]

	if sender in senders:
		if "-" in receiver:
			senders[sender]+=1
	else:
		senders[sender] = 0
		if "-" in receiver:
			senders[sender]+=1

print senders

for line in jytky:
	sender = line.partition(" ")[0]
	receiver = line.partition("-> ")[2]

	if receiver in receive_count:
		receive_count[receiver]+=1
	else:
		receive_count[receiver] = 1

print receive_count
