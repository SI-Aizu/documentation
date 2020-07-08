# Data Augmentation

[Data augmentation  |  TensorFlow Core](https://www.tensorflow.org/tutorials/images/data_augmentation)



下の画像を元にデータを拡張。

全体のコードは `augmentation.py` に記載。

![](https://user-images.githubusercontent.com/39023477/86331234-c5978280-bc83-11ea-88cc-7793e9417ef0.jpg)



## Import libraries

```py
import tensorflow as tf

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 5)
```



## Read an image

```py
image_dir_path = "images/"
image_name = "squirrel.jpg"

image_string=tf.io.read_file(image_dir_path + image_name)
image=tf.image.decode_jpeg(image_string,channels=3)
```



## show images

オリジナル画像と拡張後の画像を見比べるための関数。

```py
def visualize(original, augmented, filename):
  fig = plt.figure()
  plt.subplot(1,2,1)
  plt.title('Original image')
  plt.imshow(original	)
  plt.subplot(1,2,2)
  plt.title('Augmented image')
  plt.imshow(augmented)
  plt.savefig(image_dir_path + filename)
```



## Flip Horizontally

画像を左右反転させる。

```py
# tf.image.flip_left_right(image)
flipped = tf.image.flip_left_right(image)
visualize(image, flipped, "flipped.jpg")
```

![](https://user-images.githubusercontent.com/39023477/86384432-ae7b8380-bcc9-11ea-9cbb-6259c75d41af.jpg)

## Flip Vertically

画像を上下反転させる。

```py
# tf.image.flip_up_down(image)
flipped = tf.image.flip_up_down(image)
visualize(image, flipped, "flipped_up_down.jpg")
```

![](https://user-images.githubusercontent.com/39023477/86389148-dae6ce00-bcd0-11ea-936d-a37fbe2ba65b.jpg)

## grayscale

画像をグレイスケールにする。

```py
# tf.image.rgb_to_grayscale(images, name=None)
grayscaled = tf.image.rgb_to_grayscale(image)
visualize(image, tf.squeeze(grayscaled), "grayscaled.jpg")
```

```py
print(image.shape)
print(grayscaled.shape)
# (1066, 1600, 3)
# (1066, 1600, 1)
```

![](https://user-images.githubusercontent.com/39023477/86385330-0ff02200-bccb-11ea-89d9-2f4736568f1f.jpg)

## saturation

画像の彩度を調整する。

画像を HSV に変換した後、彩度(S) に `saturation_factor` を乗算してまた RGB に戻す。

```py
# tf.image.adjust_saturation(image, saturation_factor, name=None)
saturated = tf.image.adjust_saturation(image, 3)
visualize(image, saturated, "saturated.jpg")
```

![](https://user-images.githubusercontent.com/39023477/86388055-0cf73080-bccf-11ea-801f-98a1350b1af9.jpg)



## brightness

画像の輝度を調整する。

画像を [0,1] の浮動小数型に変換した後、`delta` を各画素に加算する。加算が終了したら元のデータ型に戻す。

```py
#tf.image.adjust_brightness(image, delta)
bright = tf.image.adjust_brightness(image, 0.4)
visualize(image, bright, "bright.jpg")
```

![](https://user-images.githubusercontent.com/39023477/86390486-18e4f180-bcd3-11ea-9da8-9b5fb2dedb8b.jpg)



## Rotation

画像を `k` * 90° 回転させる。

```py
# tf.image.rot90(image, k=1, name=None)
rotated = tf.image.rot90(image, k=1)
visualize(image, rotated, "rotated.jpg")
```

![](https://user-images.githubusercontent.com/39023477/86392953-40d65400-bcd7-11ea-9e8a-5b107902efd5.jpg)

## Crop the central region

画像を中央から `central_fraction` * 100% 切り抜く。

```py
# tf.image.central_crop(image, central_fraction)
cropped = tf.image.central_crop(image, central_fraction=0.5)
visualize(image,cropped,"cropped.jpg")
```

![](https://user-images.githubusercontent.com/39023477/86390108-70cf2880-bcd2-11ea-8a36-71ddf1f7099a.jpg)

## Apply a data augmentation randomly

ランダムにデータ拡張を適用する。

拡張の方法を関数にしておき、毎回ランダムにそれらの関数を選ぶような処理。

```py
def flip(image):
    return tf.image.flip_left_right(image)

def grayscale(image):
    return tf.image.rgb_to_grayscale(image)

def saturate(image):
    return tf.image.adjust_saturation(image, 3)

def bright(image):
    return tf.image.adjust_brightness(image, 0.4)

def rotate(image):
    return tf.image.rot90(image,k=1)

def crop(image):
    return tf.image.central_crop(image, central_fraction=0.5)
    
funcs = [flip, grayscale, saturate, bright, rotate, crop]
num = list(range(len(funcs)))
for i in range(random.randrange(1,3)):
    chosen = random.choice(num) 
    image = random.choice[funcs](image)
    num.remove(chosen)
```
