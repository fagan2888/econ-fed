from __future__ import division, print_function, absolute_import

import numpy as np
import tflearn
import tensorflow as tf
from tflearn.data_utils import to_categorical, pad_sequences

from combine import X, Y, predicted

monthly_deviations = []
rates = []
tays = []


def tay(x_element, u_n=5): # X element: [rGDPr, u, i]
	unemployment_rate = x_element[1]
	inflation_rate = x_element[2]
	rate = 1 + 1.5*inflation_rate - (unemployment_rate - u_n)
	return rate


def run():
	fed_funds = model.predict([[4.21, 4, 8]])
	print(fed_funds)

	# for index, element in enumerate(X):
	# 	rate = model.predict([element])[0][0]
	# 	rates.append(rate)
	# 	year = 1954+(index/12)

	# 	taylor_rule_rate = tay(element)

	# 	tays.append(taylor_rule_rate)


	# 	monthly_deviation = abs(rate-Y[index])
	# 	monthly_deviations.append(monthly_deviation)

	# # print(rates)
	# print(tays)
	# print(monthly_deviations)







# Network building
net = tflearn.input_data([None, 3])
net = tflearn.fully_connected(net, 10, activation='linear',
                                 regularizer='L2', weight_decay=0.0005)
net = tflearn.fully_connected(net, 1, activation='linear')
net = tflearn.regression(net, optimizer=
	tflearn.optimizers.AdaGrad(learning_rate=0.01, initial_accumulator_value=0.01), 
	loss='mean_square', learning_rate=0.05)

# Training
model = tflearn.DNN(net, checkpoint_path='tmp/')

model.load('/Users/rodrigo.castellon/Desktop/econ-fed/analysis/tmp-7000')

run()