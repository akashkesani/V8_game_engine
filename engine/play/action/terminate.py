import pygame



class Terminate:
    def __init__(self):
        self.name = 'TerminateAction'
        self.type = ['action','event']
        self.children = []
        self.entity = None
        self.entity_state = None
        self.verbose = False


    def condition_to_act(self,data = None):

        if self.entity_state == False:
            return False
        if self.entity_state.active == False:
            return False
        if data.type == pygame.QUIT:
            return True    
        if data.type == pygame.KEYDOWN:
            if data.key == pygame.K_ESCAPE:    
                return True

        return False

    def act(self,data = None):
        if (self.condition_to_act(data)):
            
            if (self.verbose):
                print("exiting")
            from sys import exit
            pygame.quit()
            exit()
            if (self.children):
                for child in self.children:
                    child.act(data)