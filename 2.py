# -*- coding: utf-8 -*-

import tensorflow as tf

# 宣告變數
# tf.Variable=>這代表變數，以下展示如何用它來顯示 0 ~ 4。您可以不斷地更改變數的值，直到您滿意為止。
B = tf.Variable(0, dtype=tf.int64)
with tf.Session() as sess:
    # 變數需要初始化
    sess.run(tf.global_variables_initializer())

    # 使用 assign 更改變數值
    for i in range(5):
        print(sess.run(B.assign(i)))
    '''
    其中，請特別注意 assign 這個函數，此函數需要經過 sess.run() 之後，才會賦予新值。
    若是把上面的迴圈改成這樣：
    
    for i in range(5):
        B.assign(i)
        print(sess.run(B))
    這樣 B 值是不會改變的，因為 assign 未被執行。
    這裡非常容易用錯，請小心。
    執行結果:
    0
    0
    0
    0
    0
    '''

    '''
    執行結果：
    0
    1
    2
    3
    4
    '''
