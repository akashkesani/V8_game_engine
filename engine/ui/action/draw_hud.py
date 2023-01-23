import pygame, sys
import random
sys.path.append("/Users/akashkesani/Desktop/projects/V8_game_engine")

from engine.actor.entity.letter import Letter
from engine.actor.action.draw_letter import DrawLetter

class DrawHUD:


    def __init__(self, ):
        
        self.name = 'Press button action'
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

        return True

    def act(self, data = None):
        
        if (self.condition_to_act()):
            
            if(self.verbose):
                print("drawing HUD")
            
            font = pygame.font.Font(None,18)
            total = font.render( self.entity_state.message1
                                 + " " + str(self.entity_state.counter1),
                                 True, (255,255,255))
            success = font.render(self.entity_state.message2 
                                  + " " +str(self.entity_state.counter2), 
                                  True,(255,255,255))
            data.blit(total, (10,10))
            data.blit(success, (10,40))

            for children in self.children:
                children.act(data)