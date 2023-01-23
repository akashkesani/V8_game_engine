

class PositionSolve:
    
    
    def __init__(self):
        
        self.name = 'Position Solve Action'
        self.types = ['loop']
        self.entity_state = None
        self.children = []
        self.verbose = False
        self.dt = 0.0
        return
    
    def condition_to_action(self):
        
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False

        return True

    def act(self,data = None):
        
        if(self.condition_to_action()):

            if (self.verbose):
                print("Assigning positions to active particles")
            
            

            for i in range(0,len(self.entity_state.position)):    
                
                if (self.verbose):
                    print(self.entity_state.position[i])
                    print("end")
                if (self.entity_state.active_particles[i]):
                    self.entity_state.position[i][0] = (self.entity_state.position[i][0] 
                                                        + self.dt 
                                                        * self.entity_state.velocity[i][0])
                    self.entity_state.position[i][1] = (self.entity_state.position[i][1]
                                                        + self.dt
                                                        * self.entity_state.velocity[i][1])
            
                if (self.verbose):
                    print(self.entity_state.position[i])


            for children in self.children:
                children.act(data)

            return