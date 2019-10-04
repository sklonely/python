# -*- coding: utf-8 -*-
import random
import gym
import gym_chrome_dino
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPool2D, Flatten, Dense, Dropout, MaxPooling2D, Conv2D
from keras.optimizers import Adam
from PIL import Image

EPISODES = 5000


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.999
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        model.add(Conv2D(
            32, 3, 3, input_shape=self.state_size, activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # Second convolutional layer
        model.add(Conv2D(32, 3, 3, activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # Third convolutional layer
        model.add(Conv2D(64, 3, 3, activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Flatten())

        model.add(Dense(output_dim=128, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma *
                          np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)


def downsample_image(A):

    B = A[22:]

    B = B.mean(axis=2)

    # B = imresize(B, size=(100, 100), interp='nearest')
    B = np.array(Image.fromarray(B).resize((100, 100)))
    # B[B < 255] = B[B < 255]-50
    # cv2.imshow("1", B/255)
    # cv2.waitKey(1)
    B = np.reshape(B, (1, 100, 100, 1))
    return B/255


if __name__ == "__main__":
    env = gym.make('ChromeDino-v0')

    state_size = (100, 100, 1)
    action_size = 3

    agent = DQNAgent(state_size, action_size)
    agent.load("cartpole-dqn.h5")
    done = False
    batch_size = 128

    for e in range(EPISODES):
        state = env.reset()

        state = downsample_image(state)
        for time in range(500):
            # env.render()
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            reward = reward + 0.1 if not done else -10
            next_state = downsample_image(next_state)
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, EPISODES, time, agent.epsilon))
                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)
        if e % 10 == 0:
            agent.save("cartpole-dqn.h5")
