import pygame


class BasicButton:
    

    def __init__(self, position_, color_, dimensions_, ):

        self.name = 'Button Entity'
        self.type = ['entity']
        self.actions = []
        self.active = True
        self.position = position_
        self.color = color_
        self.visibile = True
        self.dimensions = dimensions_
        self.clicked = False
        self.bounds = (position_[0],position_[1],position_[0] + dimensions_[0], position_[1] + dimensions_[1])

    def add_action(self, action):

        action.entity_state = self
        self.actions.append(action)




