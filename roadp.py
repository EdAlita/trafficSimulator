from scipy.spatial import distance
from collections import deque

class RoadP:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.pedestrains = deque()

        self.init_properties()

    def init_properties(self):
        self.length = distance.euclidean(self.start, self.end)
        self.angle_sin = (self.end[1]-self.start[1]) / self.length
        self.angle_cos = (self.end[0]-self.start[0]) / self.length
        # self.angle = np.arctan2(self.end[1]-self.start[1], self.end[0]-self.start[0])
        self.has_traffic_signalp = False

    def set_traffic_signalp(self, signal, group):
        self.traffic_signalp = signal
        self.traffic_signal_groupp = group
        self.has_traffic_signalp = True

    @property
    def traffic_signal_statep(self):
        if self.has_traffic_signalp:
            i = self.traffic_signal_groupp
            return self.traffic_signalp.current_cycle[i]
        return True

    def update(self, dt):
        n = len(self.pedestrains)

        if n > 0:

            # Update first vehicle
            self.pedestrains[0].update(None, dt)
            #Create a latin car mode
            if n%10==0:
                self.pedestrains[0].latinmode()

            # Update other pedestrains
            for i in range(1, n):
                lead = self.pedestrains[i-1]
                self.pedestrains[i].update(lead, dt)

             # Check for traffic signal
            if self.traffic_signal_statep:
                # If traffic signal is green or doesn't exist
                # Then let pedestrains pass
                self.pedestrains[0].unstop()
                for pedestrain in self.pedestrains:
                    pedestrain.unslow()
            else:
                # If traffic signal is red
                if self.pedestrains[0].x >= self.length - self.traffic_signalp.slow_distance:
                    # Slow pedestrains in slowing zone
                    self.pedestrains[0].slow(self.traffic_signalp.slow_factor*self.pedestrains[0]._v_max)
                if self.pedestrains[0].x >= self.length - self.traffic_signalp.stop_distance and\
                   self.pedestrains[0].x <= self.length - self.traffic_signalp.stop_distance / 2:
                    # Stop pedestrains in the stop zone
                    self.pedestrains[0].stop()