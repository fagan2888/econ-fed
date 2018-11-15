""" Linear Regression Example """

from __future__ import absolute_import, division, print_function
import numpy as np
from combine import X, Y, testX, testY

import tflearn
# Length: 768 months of data ((2018-1954)years*12 months/year) 
X = np.array(X)
Y = np.array(Y)
testX = np.array(testX)
testY = np.array(testY)
# X = X.reshape((687,3,1))
Y = Y.reshape((687,1))
# testX = testX.reshape((76,3,1))
testY = testY.reshape((76,1))
print(X.shape)
print(Y.shape)
print(testX.shape)
print(testY.shape)

# # Linear Regression graph
# input_ = tflearn.input_data(shape=[None])
# linear = tflearn.single_unit(input_)

# Building deep neural network
input_layer = tflearn.input_data(shape=[None, 3])
dense1 = tflearn.fully_connected(input_layer, 5, activation='tanh',
                                 regularizer='L2', weight_decay=0.001)
# dropout1 = tflearn.dropout(dense1, 0.8)
# dense2 = tflearn.fully_connected(dropout1, 64, activation='tanh',
#                                  regularizer='L2', weight_decay=0.001)
# dropout2 = tflearn.dropout(dense2, 0.8)
softmax = tflearn.fully_connected(dense1, 1, activation='softmax')

# Regression using SGD with learning rate decay and Top-3 accuracy
sgd = tflearn.SGD(learning_rate=0.1, lr_decay=0.96, decay_step=1000)
top_k = tflearn.metrics.Top_k(3)
net = tflearn.regression(softmax, optimizer=sgd, metric=top_k,
                         loss='categorical_crossentropy')

# Training
model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(X, Y, n_epoch=20, validation_set=(testX, testY),
          show_metric=True, run_id="dense_model")



regression = tflearn.regression(linear, optimizer='sgd', loss='mean_square',
                                metric='R2', learning_rate=0.01)
m = tflearn.DNN(regression)
m.fit(X, Y, n_epoch=1000, show_metric=True, snapshot_epoch=False)

print("\nRegression result:")
print("Y = " + str(m.get_weights(linear.W)) +
      "*X + " + str(m.get_weights(linear.b)))

print("\nTest prediction for x = 3.2, 3.3, 3.4:")
print(m.predict([3.2, 3.3, 3.4]))
# should output (close, not exact) y = [1.5315033197402954, 1.5585315227508545, 1.5855598449707031]