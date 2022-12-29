import pygame


class Circle:
    

    def __init__(self, position_, color_, radius_):

        self.name = 'Circle Entity'
        self.type = ['entity']
        self.actions = []
        self.active = True
        self.position = position_
        self.color = color_
        self.visibile = True
        self.radius = radius_

    def add_action(self, action):

        action.entity_state = self
        self.actions.append(action)


