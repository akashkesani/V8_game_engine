

class PickPosition:


    def __init__(self, index_):

        self.name = 'Pick Position Action'
        self.types = ['loop']
        self.entity_state = None
        self.children = []
        self.verbose = False
        self.index = index_
        return
    
    def condition_to_action(self):
        
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if self.index >= len(self.entity_state.position):
            if (self.verbose):
                print("particle index is beyond particles present")
            return False
        if len(self.entity_state.position[self.index]) !=2:
            if (self.verbose):
                print("particle information in particle array is incorrect")
            return False
        
        return True

    def act(self,data = None):
        
        if(self.condition_to_action()):
            if (self.verbose):
                print("Picking a particle")
            new_data = list(self.entity_state.position[self.index])
            for children in self.children:
                children.act(new_data)

            return