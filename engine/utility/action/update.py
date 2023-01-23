import pygame
import time

class Update:


    def __init__(self, ):
        
        self.name = 'Press button action'
        self.type = ['action','loop']
        self.children = []
        self.eventType = None
        self.verbose = False
        self.entity_state = None

    def condition_to_act(self, data = None):
        
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False

        return True

    def act(self, data = None):
        
        if (self.condition_to_act()):

            if (self.verbose):
                print("updating current time")

            self.entity_state.current_time = round(time.time()*1000)
    
            for children in self.children:
                children.act()