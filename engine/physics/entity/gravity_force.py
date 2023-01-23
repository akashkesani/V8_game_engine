

class GravityForce:
    
    
    def __init__(self):
        
        self.name = 'Gravity Force Entity'
        self.actions = []
        self.active = True
        self.gravity = [0.0, 0.1]
    
    def add_action(self,a):
        
        a.entity_state = self
        self.actions.append(a)