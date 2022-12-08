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
        if self.v + self.a*dt < 0:
            self.x -= 1/2*self.v*self.v/self.a
            self.v = 0
        else: 
            self.v += self.a*dt
            self.x += self.v*dt + self.a*dt*dt/2     
          
        #update acceleration
        alpha = 0
        if lead:
            delta_x = lead.x - self.x -lead.l
            delta_v = self.v - lead.v

            alpha = (self.s0 + max(0, self.T*self.v + delta_v*self.v/self.sqrt_ab) ) / delta_x

            self.a = self.a_max * (1-(self.v/self.v_max)**4 - alpha**2)

        if self.stopped:
            if self.rougue==False:
                self.a = -self.b_max*self.v/self.v_max    
            
        #Stop and Latin America funtion

    def stop(self):
        self.stopped = True

    def unstop(self):
        self.stopped = False

    def slow(self, v):
        self.v_max = v

    def unslow(self):
        self.v_max = self._v_max
    
    def latinModeOFF(self):
        self.rougue=False
    
    def latinModeOn(self):
        self.rougue=True
        