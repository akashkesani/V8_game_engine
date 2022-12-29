import pygame


class Rectangle:


    def __init__(self, height_, width_, start_x, start_y, color):
        
        self.name = ''
        self.type = []
        self.actions = []
        self.active = True
        self.height = height_
        self.width = width_
        self.start_x = start_x
        self.start_y = start_y
        self.color = color
        self.visibile = True

    def add_action(self,action):
        
        action.entity_state = self
        self.actions.append(action)
