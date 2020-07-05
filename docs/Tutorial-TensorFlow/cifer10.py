from __future__ import absolute_import, division, print_function, unicode_literals

import random

import tensorflow as tf
from tensorflow.keras import Sequential, datasets
from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D

AUTOTUNE = tf.data.experimental.AUTOTUNE
EPOCH = 30
BATCH = 128


def convert(image, label):
    image = tf.image.convert_image_dtype(image, tf.float32)
    return image, label


def augment(image, label):
    def central_crop(image, label):
        image = tf.image.resize_with_crop_or_pad(image, 40, 40)
        image = tf.image.central_crop(image, central_fraction=0.8)
        return image, label

    def random_crop(image, label):
        image = tf.image.resize_with_crop_or_pad(image, 40, 40)
        image = tf.image.random_crop(image, size=[32, 32, 3])
        return image, label

    def adjust_brightness(image, label):
        image = tf.image.adjust_brightness(image, 0.3)
        return image, label

    def random_brightness(image, label):
        image = tf.image.random_brightness(image, 0.2)
        return image, label

    def adjust_contrast(image, label):
        image = tf.image.adjust_contrast(image, 0.2)
        return image, label

    def random_contrast(image, label):
        image = tf.image.random_contrast(image, 0.2, 0.4)
        return image, label

    def adjust_hue(image, label):
        image = tf.image.adjust_hue(image, 0.2)
        return image, label

    def random_hue(image, label):
        image = tf.image.random_hue(image, 0.2)
        return image, label

    def adjust_saturation(image, label):
        image = tf.image.adjust_saturation(image, 0.5)
        return image, label

    def random_saturation(image, label):
        image = tf.image.random_saturation(image, 0.3, 0.6)
        return image, label

    image, label = convert(image, label)

    funcs = [random_crop, random_brightness, random_contrast, random_hue, random_saturation]
    """

  funcs = [central_crop, adjust_brightness,
           adjust_contrast, adjust_hue, adjust_saturation]
  """

    num = list(range(len(funcs)))
    for i in range(random.randrange(1, 3)):  # 1 or 2
        chosen = random.choice(num)
        image, label = funcs[chosen](image, label)
        num.remove(chosen)

    return image, label


def create_model():
    model = Sequential(
        [
            Conv2D(64, 3, activation="relu", input_shape=(32, 32, 3)),
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
    cifar10 = datasets.cifar10
    (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

    train_images = tf.reshape(train_images, (50000, 32, 32, 3))
    test_images = tf.reshape(test_images, (10000, 32, 32, 3))
    ds_train = tf.data.Dataset.from_tensor_slices((train_images, train_labels))
    ds_test = tf.data.Dataset.from_tensor_slices((test_images, test_labels))

    train_batches = ds_train.map(convert, num_parallel_calls=AUTOTUNE)

    for i in range(0, 50000, 1000):
        augmented_train_batches = (
            ds_train.skip(i).take(1000).map(augment, num_parallel_calls=AUTOTUNE)
        )

        train_batches = train_batches.concatenate(augmented_train_batches)

    all_train_batches = train_batches.shuffle(100000).batch(BATCH).prefetch(AUTOTUNE)

    validation_batches = ds_test.map(convert, num_parallel_calls=AUTOTUNE).batch(BATCH)

    model = create_model()
    # model.fit(augmented_train_batches, epochs=EPOCH, validation_data=validation_batches)
    model.fit(all_train_batches, epochs=EPOCH, validation_data=validation_batches)
    test_loss, test_acc = model.evaluate(validation_batches, batch_size=1, verbose=1)


if __name__ == "__main__":
    main()
