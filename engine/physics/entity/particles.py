import pygame


class Particles:
    

    def __init__(self):

        self.name = 'Particles Entity'
        self.type = ['entity']
        self.actions = []
        self.active = True
        self.position = []
        self.velocity = []
        self.acceleration = []
        self.mass = []
        self.active_particles = []
        self.visibile = True
        self.springforce = []
    def add_action(self, action):

        action.entity_state = self
        self.actions.append(action)

    def add_particle(self, position_, velocity_, mass_):
        self.position.append(position_)
        self.velocity.append(velocity_)
        self.springforce.append(True)
        self.acceleration.append([0.0,0.0])
        self.mass.append(mass_)
        self.active_particles.append(True)