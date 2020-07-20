# K-fold cross-validation

[tf.data.Dataset | Tensorflow Core](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)

日本語だと `K-分割交差検証`。データセットを`K` 個に分割してK - 1個を `training set` 、残りの1個を `validation set` とする。交差検証を行うことで、モデルの汎化性能を確認する。最終的なモデルの評価としては、K個それぞれのモデルで精度を計算し、それらの平均を取るのが一般的である。

![https://user-images.githubusercontent.com/39023477/87886742-79f22080-ca5a-11ea-9c00-16fd6508c960.jpg](https://user-images.githubusercontent.com/39023477/87886742-79f22080-ca5a-11ea-9c00-16fd6508c960.jpg)

ここでは、分割時に使用した主なメゾットを紹介する。

全体コードは `K_fold_cross_validation.py` に記載。



## take

`tf.data.Dataset` 型のとき使用でき、`count` までのデータを取得する。

```py
# take(count)
dataset = tf.data.Dataset.range(10)
dataset = dataset.take(3)
list(dataset.as_numpy_iterator())
# [0, 1, 2]
```



## skip

`tf.data.Dataset` 型のとき使用でき、`count` までのデータをスキップする。

```py
# skip(count)
dataset = tf.data.Dataset.range(10)
dataset = dataset.skip(7)
list(dataset.as_numpy_iterator())
# [7, 8, 9]
```



## concatenate

`tf.data.Dataset` 型同士を結合する。

```py
# concatenate(dataset)
a = tf.data.Dataset.range(1, 3)  # ==> [1, 2]
b = tf.data.Dataset.range(3, 6)  # ==> [3, 4, 5]
ds = a.concatenate(b)
list(ds.as_numpy_iterator())
# [1, 2, 3, 4, 5]
```