import pygame

class Person:
    def __init__(self, image, x, y):
        self.image = image
        self.food = 6
        self.water = 3
        self.shelter = 1
        self.x = x
        self.y = y
        self.wood = 0

