# -*- coding: utf-8 -*-
# BY sklonley
import tensorflow as tf
import numpy as np


def case1():  # 觀念
    # 創建 常量OP
    m1 = tf.constant([[3, 3]])
    m2 = tf.constant([[2], [3]])
    # 將M1M2相乘 矩陣
    product = tf.matmul(m1, m2)
    # 定義 Session 所有的運算只能在Session裡面執行
    with tf.Session() as sess:
        result = sess.run(product)
        print(result)


def case2():  # 基礎練習
    x = tf.Variable([1, 2])  # 變數
    init = tf.global_variables_initializer()  # 使用變數需先初始化
    a = tf.constant([3, 3])  # 常數
    sub = tf.subtract(x, a)  # OP
    add = tf.add(x, sub)  # op
    with tf.Session() as sess:
        sess.run(init)  # 初始化
        print(sess.run(sub))
        print(sess.run(add))


def case3():  # for迴圈在tensorflows
    state = tf.Variable(0, name="counter")  # 變數
    new_value = tf.add(state, 1)  # op 做state+1
    update = tf.assign(state, new_value)  # tensorFlow中不能直接給值需要賦予函數
    init = tf.global_variables_initializer()  # 使用變數需先初始化
    with tf.Session() as sess:
        sess.run(init)
        print(sess.run(state))
        for _ in range(5):
            sess.run(update)
            print(sess.run(state))


def case4():  # Fetch 可一次調用多個op
    input1 = tf.constant(3.0)
    input2 = tf.constant(3.0)
    input3 = tf.constant(3.0)
    add = tf.add(input2, input3)
    mul = tf.multiply(input1, add)
    with tf.Session() as sess:
        result = sess.run([mul, add])
        print(result)


def case5():  # Feed 可讓op在需要時再帶值
    # 創建佔位符
    input1 = tf.placeholder(tf.float32)
    input2 = tf.placeholder(tf.float32)
    output = tf.multiply(input1, input2)
    with tf.Session() as sess:
        print(sess.run(output, feed_dict={input1: [7.0], input2: [2.0]}))


def case6():
    # 創建資料模型
    x_data = np.random.rand(100)
    y_data = x_data * 0.8 + 1.2
    # 創建TF模型
    b = tf.Variable(0.)
    k = tf.Variable(0.)
    y = k * x_data + b
    # 二次代價函數
    loss = tf.reduce_mean(tf.square(y_data - y))  # 計算誤差值
    # 定義優化法
    optimizer = tf.train.GradientDescentOptimizer(0.2)
    train = optimizer.minimize(loss)
    # 使用TF開始進行實驗
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        for step in range(200):
            sess.run(train)
            if step % 20 == 0:
                print(step, sess.run([k, b, loss]))


def add_layers(inputs, input_size, output_size,
               activation_funtion=None):  # 創建一個層
    inputs = tf.cast(inputs, tf.float32)
    Weights = tf.Variable(tf.random_normal([input_size, output_size]))
    biases = tf.Variable(tf.zeros([1, output_size]) + 0.1)
    Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
    if activation_funtion is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_funtion(Wx_plus_b)
    return outputs


def tenstest():
    # 創建基礎資料
    x_data = np.random.rand(100)
    noise = np.random.normal(0, 0.05, x_data.shape)
    y_data = x_data * 0.8 + 1.2 + noise
    # 創建類神經網路
    L1 = add_layers(x_data, 1, 10, activation_funtion=tf.nn.relu)
    predition = add_layers(L1, 10, 1, activation_funtion=None)
    loss = tf.reduce_mean(
        tf.reduce_sum(tf.square(y_data - predition), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)
    init = tf.initialize_all_variables()
    # 運行圖
    with tf.Session() as sess:
        sess.run(init)
        for step in range(200):
            sess.run(train_step)
            if step % 20 == 0:
                print(step, sess.run([loss]))


case6()
