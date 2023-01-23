import pygame



class Loop:
    def __init__(self):
        self.name = ''
        self.type = ['action']
        self.children = []
        self.entity_state = None
        self.verbose = False
        self.loopRunning = True
        self.loops = 0

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
                if (self.verbose):
                    self.loops += 1
                    print ("The loop has been running for : "+ str(self.loops))
                    if(self.loops >20):
                        self.loopRunning = False

            if(self.children):
                for child in self.children:
                    child.act(data)