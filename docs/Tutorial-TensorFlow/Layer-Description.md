# Layers

## 畳み込み層 Convolutional Layer

```python
# tf.keras.layers.Conv2D(filters, kernel_size, strides=(1, 1), padding='valid', activation=None, input_shape)
input_shape = (4, 5, 5, 3) # batch, I_h, I_w, channel
x = tf.random.normal(input_shape)
y = tf.keras.layers.Conv2D(2, 3, activation='relu', input_shape=input_shape)(x)
print(y.shape)
# (4, 3, 3, 2) # batch, O_h, O_w, filter
```

<img src="https://user-images.githubusercontent.com/39023477/84355712-04df3000-abfe-11ea-83c1-13316f64af1c.jpg" style="zoom:67%;" />

## プーリング層 Pooling Layer

```python
# tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=None, padding='valid')
input_shape = (4, 5, 5, 3) # batch, I_h, I_w, channel
x = tf.random.normal(input_shape)
y = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(1, 1), padding='valid')(x)
print(y.shape)
# TensorShape([4, 4, 4, 3]) # batch, O_h, O_w, channel

```



<img src="https://user-images.githubusercontent.com/39023477/84375763-01a66d00-ac1b-11ea-83f6-6188acb911fb.jpg" style="zoom:67%;" />

## 全結合層 Fully Connected Layer

```python
# tf.keras.layers.Dense(units, activation=None)
input_shape = (4, 3, 3, 2) # batch, I_h, I_w, channel
x = tf.random.normal(input_shape)
y = tf.keras.layers.Flatten()(x)
print(y.shape)
# TensorShape([1, 18])
out = tf.keras.layers.Dense(1)(y)
print(out.shape)
# TensorShape([1, 1]) # units
```



<img src="https://user-images.githubusercontent.com/39023477/84370861-ceacab00-ac13-11ea-9113-ec1da955ca0e.jpg" style="zoom:67%;" />
