from datetime import datetime

fedfunds = open('fedfunds.txt')
inflation = open('inflation.txt')
lfpr = open('lfpr.txt')
rgdpgrowth = open('rgdpgrowth.txt')
unemployment = open('unemployment.txt')

unemployment = unemployment.readlines()
unemployment = unemployment[1:]
unemployment.reverse()

unemployment = unemployment[6:-2]

X = []


for index, elem in enumerate(unemployment):
	date = ' '.join(elem.split()[0:3])


	datetime_object = datetime.strptime(date, '%b %d, %Y')

	rate = elem.split()[3][:-1]
	rate = float(rate)

	X.append(rate)

print(X)


# Encoding dates
# date = {'year': 2018, 'month': 5}