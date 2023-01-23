import pygame



class Letter:


    def __init__(self, size_, color_, font_, position_, letter_):
        
        self.name = 'Letter Entity'
        self.type = ['entity']
        self.actions = []
        self.active = True
        self.letter = letter_
        self.size = size_
        self.color = color_
        self.font = font_
        self.position = position_
        self.visibile = True

    def add_action(self, action):
        
        action.entity_state = self
        self.actions.append(action)
        