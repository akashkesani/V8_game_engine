

class VelocitySolve:


    def __init__(self):

        self.name = 'Velocity Solve Action'
        self.types = ['loop']
        self.entity_state = None
        self.children = []
        self.verbose = True
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
                print("Assigning velocities to active particles")
            
            for children in self.children:
                children.act(self.entity_state)

            for i in range(0,len(self.entity_state.velocity)):    
                if (self.entity_state.active_particles[i]):
                    self.entity_state.velocity[i][0] = (self.entity_state.velocity[i][0] 
                                                        + (self.dt 
                                                           * self.entity_state.acceleration[i][0]))
                    self.entity_state.velocity[i][1] = (self.entity_state.velocity[i][1]
                                                        + (self.dt
                                                           * self.entity_state.acceleration[i][1]))
                    self.entity_state.acceleration[i][0] = 0
                    self.entity_state.acceleration[i][1] = 0
                if (self.verbose):
                    print(str(self.entity_state.velocity[i]) + "/n/n/n")
            return