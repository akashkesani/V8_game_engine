class OutsideRectangleCollision:

    def __init__(self):
        self.name = ''
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
                    if data.position[i][0] > self.entity_state.left_lower_corner[0] and data.position[i][0] < self.entity_state.right_upper_corner[0]:
                        if data.position[i][1] > self.entity_state.left_lower_corner[1] and data.position[i][1] < self.entity_state.right_upper_corner[1]:
                            right_time = (data.position[i][0] - self.entity_state.left_lower_corner[0])/data.velocity[i][0]
                            if right_time < 0.0:
                                right_time = 1000000000.0
                            left_time = (data.position[i][0] - self.entity_state.right_upper_corner[0])/data.velocity[i][0]
                            if left_time < 0.0:
                                left_time = 1000000000.0
                            up_time = (data.position[i][1] - self.entity_state.left_lower_corner[1])/data.velocity[i][1]
                            if up_time < 0.0:
                                up_time = 1000000000.0
                            down_time = (data.position[i][1] - self.entity_state.right_upper_corner[1])/data.velocity[i][1]
                            if down_time < 0.0:
                                down_time = 1000000000.0
                            
                            minimum_time = min(right_time,left_time,up_time,down_time)
                            if right_time == minimum_time:
                                data.position[i][0] = 2.0*self.entity_state.left_lower_corner[0] - data.position[i][0]
                                data.velocity[i][0] = -data.velocity[i][0]
                            elif left_time == minimum_time:
                                data.position[i][0] = 2.0*self.entity_state.right_upper_corner[0] - data.position[i][0]
                                data.velocity[i][0] = -data.velocity[i][0]
                            elif up_time == minimum_time:
                                data.position[i][1] = 2.0*self.entity_state.left_lower_corner[1] - data.position[i][1]
                                data.velocity[i][1] = -data.velocity[i][1]
                            elif down_time == minimum_time:
                                data.position[i][1] = 2.0*self.entity_state.right_upper_corner[1] - data.position[i][1]
                                data.velocity[i][1] = -data.velocity[i][1]

                             
            for children in self.children:
                children.act(data)
            return