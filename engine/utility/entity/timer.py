import pygame
import time

class Timer:
    

    def __init__(self):

        self.name = 'Timer'
        self.type = ['entity']
        self.actions = []
        self.active = True
        self.visibile = True
        self.start_time = round(time.time()*1000)
        self.current_time = round(time.time()*1000)

    def add_action(self, action):
        action.entity_state = self
        self.actions.append(action)