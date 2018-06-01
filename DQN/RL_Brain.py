# BY sklonley

import numpy as np
import pandas as pd
import tensorflow as tf
import time


class DQN():
    # 初始化
    def __init__(self, env):
        # init experience replay
        self.replay_buffer = deque()
        # init some parameters
        self.time_step = 0
        self.epsilon = INITIAL_EPSILON
        self.state_dim = env.observation_space.shape[0]
        self.action_dim = env.action_space.n

        self.create_Q_network()
        self.create_training_method()  # Init session
        self.session = tf.InteractiveSession()
        self.session.run(tf.initialize_all_variables())
# 创建Q网络

    def create_Q_network(self):
        # network weights
        W1 = self.weight_variable([self.state_dim, 20])
        b1 = self.bias_variable([20])
        W2 = self.weight_variable([20, self.action_dim])
        b2 = self.bias_variable([self.action_dim])
        # input layer
        self.state_input = tf.placeholder("float", [None, self.state_dim])
        # hidden layers
        h_layer = tf.nn.relu(tf.matmul(self.state_input, W1) + b1)
        # Q Value layer
        self.Q_value = tf.matmul(h_layer, W2) + b2

    def weight_variable(self, shape):
        initial = tf.truncated_normal(shape)
        return tf.Variable(initial)

    def bias_variable(self, shape):
        initial = tf.constant(0.01, shape=shape)
        return tf.Variable(initial)
# 创建训练方法

    def create_training_method(self):
        pass
# 感知存储信息

    def perceive(self, state, action, reward, next_state, done):
        pass
# 训练网络

    def train_Q_network(self):
        pass
# 输出带随机的动作

    def egreedy_action(self, state):
        pass


# 输出动作

    def action(self, state):
        pass
