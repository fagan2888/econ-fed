from datetime import datetime

fedfunds = open('fedfunds.txt')
inflation = open('inflation.txt')
lfpr = open('lfpr.txt')
rgdpgrowth = open('rgdpgrowth.txt')
unemployment = open('unemployment.txt')

fedfunds = fedfunds.readlines()
fedfunds = fedfunds[1:-3]

def fedfunds_scaleup(date):
	if date[6] == '9':
		date = date[:5] + "10" + date[7:]
		return date
	elif date[5]+date[6] == "12":
		date = date[:5] + "01" + date[7:]
		return date
	else:
		date = date[:6] + str(int(date[6])+1) + date[7:]
		return date

Y = []


for index, elem in enumerate(fedfunds):
	date = elem.split()[0]

	datetime_object = datetime.strptime(date, '%Y-%m-%d')
	rate = float(elem.split()[1])

	print(datetime_object, rate)
	Y.append(rate)

print(Y)


# Encoding dates
# date = {'year': 2018, 'month': 5}