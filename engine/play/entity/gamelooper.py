import pygame



class GameLooper:
    def __init__(self):
        self.name = 'GameLooper'
        self.type = ['entity']
        self.loopActions = []
        self.eventActions = []
        self.actions = []
        self.active = True

    def insert_action(self,action):
        action.entity_state = self
        self.actions.append(action)