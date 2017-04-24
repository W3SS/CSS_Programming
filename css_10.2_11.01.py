#Sets 10.02 and 11.01

#Set 10.02

#The Finnish tax office has released corporate tax information as open data.

#For example, in 2012 file this information is stored in format year;register ID;Corporation name;Location;Taxable income;Paid taxes;Pre taxes;Tax return;Taxes to be paid

#Check all years available for download and compute

#Which corporation had highest taxable income?
#Which corporation received highest tax returns?

#Set 11.01

#Based on the tax office information, calculate which city had highest paid taxes.

import sys, argparse, csv
from collections import defaultdict

reload(sys)
sys.setdefaultencoding('utf8')

v2012 = 'yhteiso_tuloverotus_2012.csv'
v2013 = 'yhteiso_tuloverotus_julk_2013.csv'
v2014 = 'yhteiso_tuloverotus_julk_2014.csv'
v2015 = 'yhteiso_tuloverotus_julk_2015.csv'

def highest_taxable_income(year, filename,name_col,value_col):
	
	values = {}
	with open(filename, 'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(1024), delimiters=";")
		csvfile.seek(0)
		reader = csv.reader(csvfile, dialect)

		iterreader = iter(reader)
		next(iterreader)
		for line in iterreader:
		 	values[line[name_col]] = float(line[value_col].replace(',', '.'))

	highest_taxable_income = max(values, key=values.get)
	print "In " + year + " " + highest_taxable_income + " had the highest taxable income at " + str(values[highest_taxable_income]) + " euros."

def highest_tax_returns(year, filename,name_col,value_col):
	
	values = {}
	with open(filename, 'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(1024), delimiters=";")
		csvfile.seek(0)
		reader = csv.reader(csvfile, dialect)

		iterreader = iter(reader)
		next(iterreader)
		for line in iterreader:
		 	values[line[name_col]] = float(line[value_col].replace(',', '.'))

	highest_tax_returns = max(values, key=values.get)
	print "In " + year + " " + highest_tax_returns + " had the highest tax returns with " + str(values[highest_tax_returns]) + " euros."

def city_with_most_taxes(year, filename,name_col,value_col):
	
	values = {}
	with open(filename, 'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(1024), delimiters=";")
		csvfile.seek(0)
		reader = csv.reader(csvfile, dialect)

		iterreader = iter(reader)
		next(iterreader)
		for line in iterreader:
		 	if line[name_col] in values:
				values[line[name_col]] = values[line[name_col]] + float(line[value_col].replace(',', '.'))
			else:
				values[line[name_col]] = float(line[value_col].replace(',', '.'))

	city_with_most_taxes = max(values, key=values.get)
	print "In " + year + " " + city_with_most_taxes + " had the highest tax income with " + str(values[city_with_most_taxes]) + " euros."

#10.02
highest_taxable_income("2012",v2012,2,4)	
highest_taxable_income("2013",v2013,2,4)
highest_taxable_income("2014",v2014,2,4)
highest_taxable_income("2015",v2015,2,4)

highest_tax_returns("2012",v2012,2,7)	
highest_tax_returns("2013",v2013,2,7)
highest_tax_returns("2014",v2014,2,7)
highest_tax_returns("2015",v2015,2,7)

#11.01
city_with_most_taxes("2012",v2012,3,4)

