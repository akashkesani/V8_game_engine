import pygame


class DrawButton:


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
                print("drawing rect")

            pygame.draw.rect(data, self.entity_state.color, (self.entity_state.position[0],
                             self.entity_state.position[1], self.entity_state.dimensions[0], 
                             self.entity_state.dimensions[1]))

            for children in self.children:
                children.act()
            
            

                        