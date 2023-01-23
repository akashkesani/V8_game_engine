

class EulerSolve:


    def __init__(self):

        self.name = 'Euler Solve Action'
        self.types = ['loop']
        self.entity_state = None
        self.children = []
        self.verbose = False
        self.dt = 0.1
        return
    
    def condition_to_action(self):
        
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if len(self.children) <2:
            return False

        return True

    def act(self,data = None):
        
        if(self.condition_to_action()):

            if (self.verbose):
                print("Setting the positions and velocities of active particles")

            self.children[0].dt = float(self.dt)
            self.children[1].dt = float(self.dt)
            self.children[0].act()
            self.children[1].act()

            for children in self.children:
                children.act(data)

            return