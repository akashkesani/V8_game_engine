import pygame


class DrawLetter:


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
            font = pygame.font.SysFont(self.entity_state.font,self.entity_state.size)
            img = font.render(self.entity_state.letter,True,self.entity_state.color)
            data.blit(img,self.entity_state.position)
