import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 直接關閉警告訊息

# constant可以視為tf專用的變數型態
# 其他包括Variable，placeholder
# tf.constant=>這代表常數，給定初始值之後即無法再更改。
A = tf.constant('Hello World!')
B = tf.constant(10, dtype=tf.int64)

# 使用 with 可以讓Session自動關閉
with tf.Session() as sess:

    # 在 tensorflow內要使用run，才會讓計算圖開始執行
    print(A)  # Tensor("Const:0", shape=(), dtype=string)
    print(sess.run(A))  # b'Hello World!'
    print(B)  # Tensor("Const_1:0", shape=(), dtype=int64)
    print(sess.run(B))  # 10
'''
output:
紅字是警告訊息，提醒我們可以加速 TensorFlow 的執行速度之類的，
有時候會秀出其他的警告內容，大家看看就好，不會影響執行結果的。
可使用以下兩行程式碼來關閉警告
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 直接關閉警告訊息
'''
