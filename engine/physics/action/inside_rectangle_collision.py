class InsideRectangleCollision:

    def __init__(self):
        self.name = 'inside rectangle collision'
        self.types = ['']
        self.entity_state = None
        self.children = []
        self.verbose = False
        return
    
    def condition_to_action(self,data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False

        return True

    def act(self,data):

        if(self.condition_to_action(data)):
            for i in range(0,len(data.position)):
                if data.active_particles[i]:
                    if data.position[i][0] < self.entity_state.left_lower_corner[0]:
                        data.position[i][0] = 2*self.entity_state.left_lower_corner[0] - data.position[i][0]
                        data.velocity[i][0] = - data.velocity[i][0]
                    if data.position[i][0] > self.entity_state.right_upper_corner[0]:
                        data.position[i][0] = 2* self.entity_state.right_upper_corner[0] - data.position[i][0]
                        data.velocity[i][0] = - data.velocity[i][0]
                    if data.position[i][1] < self.entity_state.left_lower_corner[1]:
                        data.position[i][1] = 2*self.entity_state.left_lower_corner[1] - data.position[i][1]
                        data.velocity[i][1] = - data.velocity[i][1] 
                    if data.position[i][1] > self.entity_state.right_upper_corner[1]:
                        data.position[i][1] = 2*self.entity_state.right_upper_corner[1] - data.position[i][1]
                        data.velocity[i][1] = - data.velocity[i][1]
                    
            for children in self.children:
                children.act(data)
            if self.verbose:
                print(self.name + "for" + self.entity_state.name)
            return