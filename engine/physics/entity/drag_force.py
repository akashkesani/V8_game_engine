

class DragForce:
    
    
    def __init__(self):
        
        self.name = 'Drag Force Entity'
        self.actions = []
        self.active = True
        self.drag_constant = 1.00
    
    def add_action(self,a):
        
        a.entity_state = self
        self.actions.append(a)