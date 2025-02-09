import sys
import numpy as np
import math
import random
import gym
import code_files

def simulate():
    global epsilon, epsilon_decay
    for episode in range(MAX_EPISODES):

        state = env.reset()
        total_reward = 0

        for t in range(MAX_TRY):
            if random.uniform(0,1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(q_table[state])
            next_state, reward, done, _ = env.step(action)
            total_reward += reward

            q_value = q_table[state][action]
            best_q = np.max(q_table[next_state])
            q_table[state][action] = (1-learning_rate) * q_value + learning_rate * (reward + gamma * best_q)
            state = next_state
            env.render()

if __name__ == "__main__":
    env = gym.make("Pygame-v0")
    MAX_EPISODES = 9999
    MAX_TRY = 1000
    epsilon = 1
    epsilon_decay = .999
    learning_rate = .1
    gamma = .6
    num_box = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
    q_table = np.zeros(num_box + (env.action_space.n,))
    simulate()