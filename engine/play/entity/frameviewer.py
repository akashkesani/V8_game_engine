import pygame


class FrameViewer:
    def __init__(self,dimensions):
        self.name = 'FrameViewerEntity'
        self.type = ['entity']
        self.actions = []
        self.active = True
        self.dimensions = dimensions
        self.window = pygame.display.set_mode(dimensions)
        self.backgroundColor = (0,0,0)
        pygame.init()

    def insert_action(self,action):
        action.entity_state = self
        self.actions.append(action)


class GameLooper:
    def __init__(self):
        self.name = 'GameLooper'
        self.type = ['entity']
        self.loopActions = []
        self.eventActions = []
        self.actions = []
        self.active = True

    def insert_action(self,action):
        action.entity_state = self
        self.actions.append(action)


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




class XXXX:
    def __init__(self):
        self.name = ''
        self.type = ['entity']
        self.actions = []
        self.active = True

    def insert_action(self,action):
        action.entity_state = self
        self.actions.append(action)



class YYYYY:
    def __init__(self):
        self.name = ''
        self.type = ['action']
        self.children = []
        self.entity = None
        self.entity_state = None
        self.verbose = True


    def condition_to_act(self):
        if self.entity == None:
            return False
        if self.entity_state == False:
            return False
        

        return True

    def act(self,data = None):
        if (self.condition_to_act):


            if(self.children):
                for child in self.children:
                    child.act(data)

        




