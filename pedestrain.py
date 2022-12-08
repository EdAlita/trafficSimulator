import numpy as np

class Pedestrain:
    def __init__(self, config={}):
        #set default configuration
        self.set_default_config()

        #Update configuration
        for attr, val, in config.items():
            setattr(self, attr, val)

        #Calculate properties
        self.init_properties()

    def set_default_config(self):
        self.l = 2
        self.s0 = 2
        self.T = 1
        self.v_max = 8.3
        self.a_max = 0.9
        self.b_max = 4.07

        self.path = []

        self.x = 0
        self.v = self.v_max
        self.a = 0
        self.stopped = False
        self.rougue = False

    def init_properties(self):
        self.sqrt_ab = 2*np.sqrt(self.a*self.b_max)
        self._v_max = self.v_max
    
    def update(self, lead, dt):
        #update position and velocity

        #update acceleration

        #Stop and Latin America funtion

        return


        