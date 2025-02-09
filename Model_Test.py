from keras.datasets import cifar10
import keras.utils as utils
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
supernum = 2
labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

(_, _), (x_test, y_test) = cifar10.load_data()

x_test = x_test.astype('float32') / 255.0
y_test = utils.to_categorical(y_test)

model = load_model("Image_Classifier.h5")

# evaluation phase

# results = model.evaluate(x=x_test, y=y_test)
# print("Test loss:", results[0])
# print("Test accuracy:", results[1])


test_image_data = np.asarray([x_test[supernum]])

prediction = model.predict(x=test_image_data)
max_index = np.argmax(prediction[0])
print("Prediction:", labels[max_index])
plt.imshow(x_test[supernum])
plt.show()
