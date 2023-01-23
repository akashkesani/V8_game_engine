class SpringForceAction:

    def __init__(self):
        self.name = 'spring force action'
        self.types = ['force']
        self.entity_state = None
        self.children = []
        self.verbose = True
        return
    
    def condition_to_action(self,data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        if data == None:
            return False

        return True

    def act(self,data):
        if(self.condition_to_action(data)):
            total_mass = 0.0
            center_of_mass = [0.0,0.0]
            for i in range(0,len(data.acceleration)):
                if (data.active_particles[i] and data.springforce[i]):
                    total_mass = total_mass + data.mass[i]
                    center_of_mass[0] = (center_of_mass[0] 
                                        + data.mass[i] * data.position[i][0])
                    center_of_mass[1] = (center_of_mass[1]
                                         + data.mass[i] * data.position[i][1])
            
            center_of_mass[0] = center_of_mass[0]/total_mass
            center_of_mass[1] = center_of_mass[1]/total_mass
            
            if(self.verbose):
                print("This is center of mass")
                print(center_of_mass)
                print("\n\n")

            for i in range(0,len(data.acceleration)):
                if (data.active_particles[i] and data.springforce[i]):
                    accel = [0.0,0.0]
                    accel[0] = (((center_of_mass[0] - data.position[i][0])
                                                     * self.entity_state.spring_constant 
                                                     / data.mass[i]))/80

                    accel[1] = (((center_of_mass[1] - data.position[i][1])
                                                     * self.entity_state.spring_constant
                                                     / data.mass[i]))/80

                    data.acceleration[i][0] = data.acceleration[i][0] + accel[0]
                    data.acceleration[i][1] = data.acceleration[i][1] + accel[1]
                    

            for children in self.children:
                
                children.act(data)
            
            if self.verbose:
                print(self.name + "for" + self.entity_state.name)

            return