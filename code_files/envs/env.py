from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random 
from code_files.envs.Game import Game

class CustomEnv(Env):
    def __init__(self):
        self.pygame = Game
        #[left, right, up, down, build]
        self.action_space = Discrete(5)
        #[x,y,food, water shelter]
        self.observation_space = Box(
            low=0,
            high=np.array([320,320,6,3,1]),
            dtype=np.int16
        )
        self.length = 60
    def step(self, action):
        self.pygame.action(action)
        obs = self.pygame.observe()
        reward = self.pygame.evaluate()
        done = self.pygame.is_done()
        return obs, reward, done, {}
    def render(self, mode="human", close = False):
        self.pygame.view()
    def reset(self):
        del self.pygame
        self.pygame = Game()
        obs = self.pygame.observe()
        return obs
