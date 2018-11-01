# -*- coding: utf-8 -*-

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 直接關閉警告訊息

# 宣告占位符
C = tf.placeholder(dtype=tf.int64)
D = tf.placeholder(dtype=tf.int64)
E = tf.placeholder(dtype=tf.int64)

F = D + E

with tf.Session() as sess:
    # 可以一次填充所有的占位符
    result = sess.run(F, feed_dict={C: 10, D: 20, E: 30})
    print(result)  # 50

    # 或者只填充計算所需要的
    result = sess.run(F, feed_dict={D: 20, E: 30})
    print(result)  # 50

    '''
    這段程式會使系統報錯！
    計算所需的占位符不能為空，每次執行 sess.run() 都要填充，
    占位符不是變數，不會留存上次填充的資料。
    result = sess.run(F, feed_dict={E: 30})
    print(result)
    '''
'''
我們可以一次填充所有的占位符，也可以只填充計算所需要的。
舉凡計算會用到的占位符每次執行都需要填充，因為占位符不會保存上次填充的結果。

例:

假設每次玩要投 10 元，累積到 200 元就保證取物，其中 200 元的設定是常數。
投 10 元這個動作，就是填充占位符，投一次就玩一次。

每投一次錢，都會更新機器內的變數！
直到該變數累積至 200 元，就改變系統的狀態：也就是保證取物。

當然了，這只是一種比喻，占位符通常代表了更多的意義，
像是輸入值、外部參數等，不會僅單純地表達啟動或是不啟動兩種狀態。

'''
