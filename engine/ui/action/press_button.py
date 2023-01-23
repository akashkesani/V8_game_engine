import pygame


class PressButton:


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
            if data.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if(mx<self.entity_state.bounds[0]):
                    return False
                elif (mx > self.entity_state.bounds[2]):
                    return False
                elif (my < self.entity_state.bounds[1]):
                    return False
                elif (my > self.entity_state.bounds[3]):
                    return False
                else:
                    print("button clicked")
                    self.entity_state.clicked = True
                    for children in self.children:
                        children.act(data)

