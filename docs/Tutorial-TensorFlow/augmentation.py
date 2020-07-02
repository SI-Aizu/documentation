import tensorflow as tf

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 5)

def visualize(original, augmented, filename):
  fig = plt.figure()
  plt.subplot(1,2,1)
  plt.title('Original image')
  plt.imshow(original)

  plt.subplot(1,2,2)
  plt.title('Augmented image')
  plt.imshow(augmented)
  plt.savefig(image_dir_path + filename)

image_dir_path = "images/"
image_name = "squirrel.jpg"
image_string=tf.io.read_file(image_dir_path + image_name)
image=tf.image.decode_jpeg(image_string,channels=3)

flipped = tf.image.flip_left_right(image)
visualize(image, flipped, "flipped_left_right.jpg")

flipped = tf.image.flip_up_down(image)
visualize(image, flipped, "flipped_up_down.jpg")

grayscaled = tf.image.rgb_to_grayscale(image)
visualize(image, tf.squeeze(grayscaled), "grayscaled.jpg")

saturated = tf.image.adjust_saturation(image, 3)
visualize(image, saturated, "saturated.jpg")

bright = tf.image.adjust_brightness(image, 0.4)
visualize(image, bright, "bright.jpg")

rotated = tf.image.rot90(image,k=1)
visualize(image, rotated, "rotated.jpg")

cropped = tf.image.central_crop(image, central_fraction=0.5)
visualize(image,cropped,"cropped.jpg")
