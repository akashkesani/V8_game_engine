import pygame


class PutPosition:


    def __init__(self):
        
        self.name = 'Put Initial Position Action'
        self.type = ['action']
        self.children = []
        self.eventType = None
        self.verbose = False
        self.entity_state = None

    def condition_to_act(self, data = None):
        
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if self.entity_state.visibile == False:
            return False
        
        return True

    def act(self, data = None):
        
        if (self.condition_to_act()):
            
            if (self.verbose):
                print ("setting the position of the circles entity")

            for i in range(0,len(self.entity_state.position)):
                self.entity_state.position = data

            for child in self.children:
                child.act(data)
