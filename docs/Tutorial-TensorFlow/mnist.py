from __future__ import absolute_import, division, print_function, unicode_literals

from tensorflow.keras import datasets
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import Sequential

EPOCH = 5
BATCH = 64

mnist = datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))

train_images = train_images / 255.0
test_images = test_images / 255.0

model = Sequential(
    [
        Conv2D(64, 3, activation="relu", input_shape=(28, 28, 1)),
        Conv2D(64, 3, activation="relu"),
        MaxPooling2D(),
        Dropout(0.2),
        Conv2D(64, 3, activation="relu"),
        Conv2D(64, 3, activation="relu"),
        MaxPooling2D(),
        Dropout(0.2),
        Flatten(),
        Dense(512, activation="relu"),
        Dense(10, activation="softmax"),
    ]
)


model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(
    x=train_images,
    y=train_labels,
    steps_per_epoch=len(train_images) // BATCH,
    batch_size=BATCH,
    epochs=EPOCH,
)

test_loss, test_acc = model.evaluate(x=test_images, y=test_labels, batch_size=1, verbose=1)
