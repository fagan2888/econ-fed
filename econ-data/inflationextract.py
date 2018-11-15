from __future__ import division
from datetime import datetime

fedfunds = open('fedfunds.txt')
inflation = open('inflation.txt')
lfpr = open('lfpr.txt')
rgdpgrowth = open('rgdpgrowth.txt')
unemployment = open('unemployment.txt')

inflation = inflation.readlines()
print(inflation)

X = []

for index, elem in enumerate(inflation): # for each year
	year = int(elem.split()[0])

	rates = [float(x) for x in elem.split()[1:]]
	rates = rates[:-1]

	for j, r in enumerate(rates):
		datetime_string = '{} {}'.format(str(year), str(j+1))
		print(datetime_string)
		datetime_object = datetime.strptime(datetime_string, '%Y %m')
		rate = r
		X.append(rate)

print(X)
# THIS WILL OUTPUT FROM 1954 MONTH 1 TO 2017 MONTH 12, ADJUST MANUALLY

# Encoding dates
# date = {'year': 2018, 'month': 5}