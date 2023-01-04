from pedestrain import Pedestrain
from numpy.random import randint

class PedestrainGenerator:
    def __init__(self, sim, config={}):
        self.sim = sim

        # Set default configurations
        self.set_default_config()

        # Update configurations
        for attr, val in config.items():
            setattr(self, attr, val)

        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        """Set default configuration"""
        self.pedestrain_rate = 20
        self.pedestrains = [
            (1, {})
        ]
        self.last_added_time = 0

    def init_properties(self):
        self.upcoming_pedestrain = self.generate_pedestrain()

    def generate_pedestrain(self):
        """Returns a random pedestrain from self.pedestrains with random proportions"""
        total = sum(pair[0] for pair in self.pedestrains)
        r = randint(1, total+1)
        
        for (weight, config) in self.pedestrains:
            r -= weight
            if r <= 0:
                return Pedestrain(config)

    def update(self):
        """Add pedestrains"""
        if self.sim.t - self.last_added_time >= 60 / self.pedestrain_rate:
            # If time elasped after last added pedestrain is
            # greater than pedestrain_period; generate a pedestrain
            roadp = self.sim.roadsp[self.upcoming_pedestrain.path[0]]      
            if len(roadp.pedestrains) == 0\
               or roadp.pedestrains[-1].x > self.upcoming_pedestrain.s0 + self.upcoming_pedestrain.l:
                # If there is space for the generated pedestrain; add it
                self.upcoming_pedestrain.time_added = self.sim.t
                roadp.pedestrains.append(self.upcoming_pedestrain)
                # Reset last_added_time and upcoming_pedestrain
                self.last_added_time = self.sim.t
            n = randint(1,10)
            self.upcoming_pedestrain = self.generate_pedestrain()