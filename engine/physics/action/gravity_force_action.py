class GravityForceAction:

    def __init__(self):
        self.name = 'Gravity Force Action'
        self.types = ['loop']
        self.entity_state = None
        self.children = []
        self.verbose = False
        return
    
    def condition_to_action(self,data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if(data) == None:
            return False

        return True

    def act(self,data):

        if(self.condition_to_action(data)):
            
            for i in range(0,len(data.acceleration)):
                if data.active_particles[i]:
                    data.acceleration[i][0] = (data.acceleration[i][0] 
                                               + self.entity_state.gravity[0])
                    data.acceleration[i][1] = (data.acceleration[i][1] 
                                              + self.entity_state.gravity[1])
                    if(self.verbose):
                        print ( data.acceleration[i][0] )
                        print ( data.acceleration[i][1] )
                        print("\n\n\n")
            for children in self.children:
                children.act(data)
            
            if(self.verbose):
                print ( self.name + "for" +self.entity_state.name)
            
            return