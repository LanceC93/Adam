import pygame

class Person:
    def __init__(self, image, x, y):
        self.image = image
        self.food = 100
        self.water = 33
        self.shelter = 10
        self.x = x
        self.y = y