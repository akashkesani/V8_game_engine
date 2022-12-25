import pygame



class Display:
    def __init__(self):
        self.name = 'DisplayAction'
        self.type = ['action','loop']
        self.actions = []
        self.eventType = None
        self.entity_state = None
        self.children = []
        self.verbose = False

    def condition_to_act(self,data = None):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        
        return True
    def act(self,data = None):
        if (self.condition_to_act,data):
            pygame.display.update()
            self.entity_state.window.fill(self.entity_state.backgroundColor)
            if(self.verbose):
                print('drawing window of size '+str(self.entity_state.dimensions))
            if(self.children):
                for child in self.children:
                        child.act(self.entity_state.window)