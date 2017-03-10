import os
from keras.models import model_from_json
from keras.datasets import imdb

top_words = 10000
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=top_words)

json_file = open("LSTM/model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
## load saved model and weights
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("LSTM/model.h5")
print "Loaded model from disk"


## predict the test data
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
scores = loaded_model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))