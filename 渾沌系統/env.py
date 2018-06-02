# BY sklonley
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x1 = 0.1
x2 = 0.2
x3 = 0.3
x = []
y = []
for i in range(500):
    print(x1)
    x1 = 1.7 - x2**2 - 0.1 * x3
    x2 = x1 + 0.1
    x3 = x2

    x.append([x1])
    y.append(i)

x_data = np.array(x[0:499])
y_data = np.array(x[1:500])

print(x_data)


def add_layers(inputs, input_size, output_size, activation_funtion=None):  # 創建一個層
    inputs = tf.cast(inputs, tf.float32)
    Weights = tf.Variable(tf.random_normal([input_size, output_size]))
    biases = tf.Variable(tf.zeros([1, output_size]) + 0.1)
    Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)

    if activation_funtion is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_funtion(Wx_plus_b)
    return outputs


def tenstest(x_data, y_data):
    # 創建類神經網路
    L1 = add_layers(x_data, 1, 500, activation_funtion=tf.nn.relu)
    L2 = add_layers(L1, 500, 100, activation_funtion=tf.nn.relu)
    predition = add_layers(L2, 100, 1, activation_funtion=None)
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_data - predition), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.00001).minimize(loss)
    init = tf.initialize_all_variables()
    # 運行圖
    with tf.Session() as sess:
        sess.run(init)
        for step in range(50000):
            sess.run(train_step)
            if step % 20 == 0:
                print(step, sess.run([loss]))
        print(sess.run(predition))
        plt.plot(sess.run(predition), ".", y_data, "^")
        plt.show()


tenstest(x_data, y_data)
