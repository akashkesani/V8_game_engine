import pygame


class Rectangle:


    def __init__(self, height_, width_, position_, color):
        
        self.name = ''
        self.type = []
        self.actions = []
        self.active = True
        self.height = height_
        self.width = width_
        self.start_x = position_[0]
        self.start_y = position_[1]
        self.color = color
        self.visibile = True

    def add_action(self,action):
        
        action.entity_state = self
        self.actions.append(action)
