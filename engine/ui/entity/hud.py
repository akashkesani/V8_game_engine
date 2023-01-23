import pygame


class Hud:
    

    def __init__(self):

        self.name = 'Heads up display'
        self.type = ['entity']
        self.actions = []
        self.active = True
        self.visibile = True
        self.message1 = 'Success Counter'
        self.message2 = 'Total Counter'
        self.counter1 = 0
        self.counter2 = 0

    def add_action(self, action):
        action.entity_state = self
        self.actions.append(action)


