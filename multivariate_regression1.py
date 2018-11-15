from __future__ import division, print_function, absolute_import

import numpy as np
import tflearn
import tensorflow as tf
from tflearn.data_utils import to_categorical, pad_sequences

from combine import X, Y

# Y = np.array(Y).reshape((len(Y),1)) # KEY

# Network building
net = tflearn.input_data([None, 3])
net = tflearn.fully_connected(net, 10, activation='linear',
                                 regularizer='L2', weight_decay=0.0005)
net = tflearn.fully_connected(net, 1, activation='linear')
net = tflearn.regression(net, optimizer=
	tflearn.optimizers.AdaGrad(learning_rate=0.01, initial_accumulator_value=0.01), 
	loss='mean_square', learning_rate=0.05)

# Training
model = tflearn.DNN(net, tensorboard_verbose=1, checkpoint_path='tmp/')
model.fit(X, Y, n_epoch=1000, show_metric=True,
          batch_size=100)


print(model.predict([[2.58, 3.9, 2.5]]),[Y[-1]])