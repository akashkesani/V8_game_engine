

class RectangleCollider:
    
    
    def __init__(self, left_lower_corner_ = [0.0, 0.0], right_upper_corner_ = [100.0, 100.0] ):
        
        self.name = 'Rectangle Collider Entity'
        self.actions = []
        self.active = True
        self.left_lower_corner = left_lower_corner_
        self.right_upper_corner = right_upper_corner_
        self.verbose = False
    
    def add_action(self,a):
        
        a.entity_state = self
        self.actions.append(a)