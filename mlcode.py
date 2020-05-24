#loading the dataset
from keras.datasets import mnist
dataset = mnist.load_data('mymnist.db')
train , test = dataset
X_train , y_train = train
X_test , y_test = test
X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
from keras.utils.np_utils import to_categorical
y_train_cat = to_categorical(y_train)
y_test= to_categorical(y_test)
#Adding layers
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import adam
model = Sequential()
i=1
n=4
for i in range(i):
	model.add(Convolution2D(filters=n, 
                          kernel_size=(3,3), 
                          activation='relu',
                          input_shape=(28,28,1)
                           ))
	n=n*2
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=20, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.summary()
model.compile( optimizer = adam(lr=0.01), loss='categorical_crossentropy', metrics=['accuracy'])
trained_model=model.fit(X_train, y_train_cat, epochs=1, validation_data=(X_test,y_test))
acc=trained_model.history['accuracy'][-1:][0]
accuracy=acc*100
print("Accuracy of the model is =",accuracy)
#saving the model accuracy inside output.txt file
file=open("/cnndata/output.txt","w")
file.write(str(int(accuracy)))
file.close()
print("saved successfully in output.txt file")