import pygame



class Loop:
    def __init__(self):
        self.name = ''
        self.type = ['action']
        self.children = []
        self.entity_state = None
        self.verbose = True
        self.loopRunning = True

    def condition_to_act(self):
        if self.entity == None:
            return False
        if self.entity_state == False:
            return False
        

        return True

    def act(self,data = None):
        if (self.condition_to_act):
            while(self.loopRunning):
                if(self.entity_state.loopActions):
                    for action in self.entity_state.loopActions:
                        action.act()
                for event in pygame.event.get():
                    for action in self.entity_state.eventActions:
                        action.act(event) 

            if(self.children):
                for child in self.children:
                    child.act(data)