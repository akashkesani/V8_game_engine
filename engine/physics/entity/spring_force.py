

class SpringForce:
    
    
    def __init__(self):
        
        self.name = 'Spring Force Entity'
        self.actions = []
        self.active = True
        self.spring_constant = 0.5
    
    def add_action(self,a):
        
        a.entity_state = self
        self.actions.append(a)