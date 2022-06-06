import tensorflow
import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
import matplotlib.pyplot as plt
import numpy
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# create model
model = Sequential()
#model.add(Dropout(0.2))
model.add(Dense(100, input_dim=8, activation='relu'))
model.add(Dense(80, activation='relu'))
#model.add(Dense(0.2))
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
history = model.fit(X, Y, validation_split=0.53, epochs=500, batch_size=50, verbose=0)
# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'],color='b')
plt.plot(history.history['val_accuracy'],color='g')
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['training', 'validation'], loc='upper left')
plt.grid(color = 'grey', linestyle = '--', linewidth = 1.0)
plt.show()
# summarize history for loss
plt.plot(history.history['loss'],color='b')
plt.plot(history.history['val_loss'], color='g')
plt.title('overall classification loss')
plt.ylabel('average loss')
plt.xlabel('epoch')
plt.legend(['training', 'validation'], loc='upper left')
plt.grid(color = 'grey', linestyle = '--', linewidth = 1.0)
plt.show()