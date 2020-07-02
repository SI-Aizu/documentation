# Original Layer

TensorFlow を使用してオリジナルネットワークを構築。MNIST データに対してモデルの学習・推論を行う。

全体のコードは `mnist.py` に記載。 

## Import Libralies

```py
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow.keras import datasets
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import Sequential
```

## Parameters

エポック数とバッチ数を設定。

```py
EPOCH = 5
BATCH = 64
```



## Network

使用するネットワーク全体像。各層については [Layers](./Layers) を参照。

![](https://user-images.githubusercontent.com/39023477/86253506-9b948080-bbef-11ea-99b5-444d3f4f219b.jpg)

```py
model = Sequential([
  	Conv2D(64, 3, activation='relu', input_shape=(28, 28, 1)),
  	Conv2D(64, 3, activation='relu'),
  	MaxPooling2D(),
  	Dropout(0.2),
  	Conv2D(64, 3, activation='relu'),
  	Conv2D(64, 3, activation='relu'),
  	MaxPooling2D(),
  	Dropout(0.2),
  	Flatten(),
  	Dense(512, activation='relu'),
  	Dense(10, activation='softmax')
])
```



## Download mnint

`mnist` をスクリプト内でダウンロードする。

```py
mnist = datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
```



## Preprocessing

ネットワークで使用するために reshape する。

```py
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))
```

画像データのため 255 で除算して正規化する。

```py
train_images = train_images / 255.0
test_images = test_images / 255.0
```



## Compile and Train

```py
model.compile(optimizer='adam', 
							loss='sparse_categorical_crossentropy',
							metrics=['accuracy'])

model.fit(x=train_images, y=train_labels,
					steps_per_epoch=len(train_images) // BATCH,
					batch_size=BATCH, epochs=EPOCH
)
```



## Test the model

```py
test_loss, test_acc = model.evaluate(x=test_images, y=test_labels, batch_size=1, verbose=1)
```



## Run the mnist.py

```py
python3 mnist.py
```



```py
## train info
Epoch 1/5
937/937 [==============================] - 5s 5ms/step - loss: 0.1384 - accuracy: 0.9557
Epoch 2/5
937/937 [==============================] - 5s 5ms/step - loss: 0.0435 - accuracy: 0.9869
Epoch 3/5
937/937 [==============================] - 5s 5ms/step - loss: 0.0322 - accuracy: 0.9896
Epoch 4/5
937/937 [==============================] - 5s 5ms/step - loss: 0.0267 - accuracy: 0.9915
Epoch 5/5
937/937 [==============================] - 5s 5ms/step - loss: 0.0213 - accuracy: 0.9934

## test info
10000/10000 [==============================] - 22s 2ms/step - loss: 0.0231 - accuracy:0.9928
```

Test data に対して **99.28%** を達成。
