class XXXX:
    def __init__(self):
        self.name = ''
        self.type = ['entity']
        self.actions = []
        self.active = True

    def insert_action(self,action):
        action.entity_state = self
        self.actions.append(action)



class YYYYY:
    def __init__(self):
        self.name = ''
        self.type = ['action']
        self.children = []
        self.entity = None
        self.entity_state = None
        self.verbose = True


    def condition_to_act(self):
        if self.entity == None:
            return False
        if self.entity_state == False:
            return False
        

        return True

    def act(self,data = None):
        if (self.condition_to_act):


            if(self.children):
                for child in self.children:
                    child.act(data)
