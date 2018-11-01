# -*- coding: utf-8 -*-
'''
tf.placeholder
這代表占位符。
TensorFlow 為了讓我們更方便的導入資料而設計的函數。
先重複一次2.py，改用tf.placeholder來顯示 0 ~ 4。
'''
import tensorflow as tf

# 宣告占位符
C = tf.placeholder(dtype=tf.int64)

with tf.Session() as sess:
    for i in range(5):
        result = sess.run(C, feed_dict={C: i})
        print(result)
'''
上面比較特別的地方是，占位符可以使用 feed_dict 來賦值，
這項功能，可以讓我們在訓練模型時能輕鬆地輸入資料。
'''
