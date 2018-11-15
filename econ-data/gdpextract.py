from __future__ import division
from datetime import datetime


fedfunds = open('fedfunds.txt')
inflation = open('inflation.txt')
lfpr = open('lfpr.txt')
rgdpgrowth = open('rgdpgrowth.txt')
unemployment = open('unemployment.txt')

rgdpgrowth = rgdpgrowth.readlines()
rgdpgrowth.reverse()
rgdpgrowth = rgdpgrowth[2:]


def calculate_two_intermediate_points(element1,element2):
	unix_gap = element2['unix_time'] - element1['unix_time']

	unix_time_1 = element1['unix_time'] + unix_gap/3
	unix_time_2 = element1['unix_time'] + 2/3*unix_gap

	datetime_1 = datetime.fromtimestamp(unix_time_1)
	datetime_2 = datetime.fromtimestamp(unix_time_2)

	rate_gap = element2['rate'] - element1['rate']
	
	rate_1 = element1['rate'] + rate_gap/3
	rate_2 = element1['rate'] + 2/3*rate_gap
	



	intermediate_1 = {'unix_time': unix_time_1, 'date': datetime_1, 'rate': rate_1}
	intermediate_2 = {'unix_time': unix_time_2, 'date': datetime_2, 'rate': rate_2}

	return [intermediate_1, intermediate_2]

X = []

for index, elem in enumerate(rgdpgrowth):
	date = elem.split('\t')[0]
	datetime_object = datetime.strptime(date, '%b %d, %Y')
	unix_time = (datetime_object-datetime(1970,1,1)).total_seconds()


	b = elem.split('\t')[1]
	rate = float(b[:b.find('%')])

	X.append({'unix_time': unix_time, 'date': datetime_object, 'rate': rate})


X2 = []

for index, elem in enumerate(X):
	X2.append(elem)
	if index+1 >= len(X):
		break
	intermediate_points = calculate_two_intermediate_points(X[index], X[index+1])
	X2.append(intermediate_points[0])
	X2.append(intermediate_points[1])

X3 = []
for index, elem in enumerate(X2):
	X3.append(elem['rate'])
# print(X3)
print(X2)
# print(len(X2))
# Encoding dates
# date = {'year': 2018, 'month': 5}