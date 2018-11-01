import tensorflow as tf

# 宣告常數A&B，後面的name參數，是要繪製tensorboard時所使用的名稱。
# 若沒有指定，或是重複名稱，則tensorboard會自動修改。
A = tf.constant(50, name='const_A')
B = tf.constant(100, name='const_B')

with tf.Session() as sess:
    # 就是這邊！
    # 使用 "with tf.name_scope('Run'):" 這句話可以畫出Run這個步驟。
    with tf.name_scope('Run'):
        B = sess.run(A+B)
    print(B)

    # 畫好步驟之後，要使用"tf.summary.FileWriter"把檔案寫到目標資料夾，
    # 第二個參數表示要把整個圖層放到graph參數內，這樣才能用tensorboard畫出來。
    # 他會在當前目錄底下的tensorBoard目錄創建一個events.out.tfevents.xxxxxxxxxx(一連串的數字).(主機名稱)的檔案
    train_writer = tf.summary.FileWriter(
        'tensorBoard', sess.graph)
    train_writer.close()

'''
TensorBoard
TensorBoard 除了可以繪製計算圖之外，還能夠記錄在訓練過程中的參數變化及展示訓練資料庫的影像。
1. 把欲顯示出來的步驟使用 " tf.name_scope " 包起來。
2. 接著使用 tf.summary.FileWriter 函數輸出到目標資料夾。

確認沒問題後，在指令列下命令：

$tensorboard --logdir=C:\Users\zyting\Desktop\tensorflow\tensorBoard
TensorBoard 0.1.8 at http://DESKTOP-TQ84H0S:6006 (Press CTRL+C to quit)

這個指令的格式是：
$ tensorboard --logdir=(your path)

按下確認後，tensorboard就會把你專屬的計算圖輸出到網頁，網址是：
"http://(your ip):6006"

如果網頁打不開，可以懷疑是防火牆的問題。
要打開防火牆，請使用以下指令，把防火牆關了：
# firewall-cmd --zone=public --add-port=6006/tcp
# service firewalld restart

'''
