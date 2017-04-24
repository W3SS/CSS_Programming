#Set 10.04

#More
#Using BeautifulSoup, figure which of the discussions in Vauva.fi forums received most responses. 
#E.g. http://www.vauva.fi/keskustelu/alue/perhe_ja_arki

from bs4 import BeautifulSoup
import urllib2
import re
from collections import OrderedDict

url = urllib2.urlopen("http://www.vauva.fi/keskustelu/alue/perhe_ja_arki?sort=comment")
content = url.read()
soup = BeautifulSoup(content,"html.parser")

# threads = soup.find_all("div", class_="views-table cols-4")
even_rows = soup.find_all("div", class_="row even")
odd_rows = soup.find_all("div", class_="row odd")
first = soup.find_all("div", class_="row odd views-row-first")
last = soup.find_all("div", class_="row even views-row-last")
most_commented = {}

for element in even_rows:
	most_commented[element.a.get_text()] = element.find(class_="value").get_text()

for element in odd_rows:
	most_commented[element.a.get_text()] = element.find(class_="value").get_text()

for element in first:
	most_commented[element.a.get_text()] = element.find(class_="value").get_text()

for element in last:
	most_commented[element.a.get_text()] = element.find(class_="value").get_text()

most_commented = {key.strip('Lukittu '): item.strip() for key, item in most_commented.items()}

print "The most commented threads are, starting from highest to lowest:"
for key, value in sorted(most_commented.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)




