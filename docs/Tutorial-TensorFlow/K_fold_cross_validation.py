from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow.keras import Sequential, datasets
from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D

AUTOTUNE = tf.data.experimental.AUTOTUNE
EPOCH = 5
BATCH = 128
K = 5


def convert(image, label):
    image = tf.image.convert_image_dtype(image, tf.float32)
    return image, label


def create_model():
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
            Dense(256, activation="relu"),
            Dense(10, activation="softmax"),
        ]
    )

    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model


def main():
    mnist = datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    num_train_images = train_images.shape[0]
    train_images = tf.reshape(train_images, (60000, 28, 28, 1))
    ds_train = tf.data.Dataset.from_tensor_slices((train_images, train_labels)).map(
        convert, num_parallel_calls=AUTOTUNE
    )
    tmp_ds_train = ds_train
    all_acc = []

    for y in range(K):
        ds_train = tmp_ds_train
        train_batches = ds_train.take(0)
        validation_batches = ds_train.take(0)

        for x in range(K):
            if y == x:
                validation_batches = ds_train.take(num_train_images // K).batch(BATCH)

            else:
                part_train_batches = ds_train.take(num_train_images // K)

                train_batches = train_batches.concatenate(part_train_batches)
            ds_train = ds_train.skip(num_train_images // K)

        model = create_model()
        model.fit(train_batches.batch(BATCH), epochs=EPOCH, validation_data=validation_batches)
        test_loss, test_acc = model.evaluate(validation_batches, batch_size=1, verbose=0)
        all_acc.append(test_acc)

    avg_acc = 0
    for i in range(len(all_acc)):
        print("{}-th accracy: {:.3f}".format(i + 1, all_acc[i]))
        avg_acc += all_acc[i]

    print("average accuracy: {:.3f}".format(avg_acc / K))


if __name__ == "__main__":
    main()
