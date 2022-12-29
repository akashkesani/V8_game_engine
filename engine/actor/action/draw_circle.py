import pygame


class DrawCircle:


    def __init__(self, ):
        
        self.name = 'Draw Letter'
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
            pygame.draw.circle(data, self.entity_state.color,
                               self.entity_state.position, self.entity_state.radius)
            if(self.children):
                for child in self.children:
                    child.act(data)
                    