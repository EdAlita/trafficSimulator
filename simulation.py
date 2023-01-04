from road import Road
from roadp import RoadP
from copy import deepcopy
from vehicle_generator import VehicleGenerator
from pedestrain_generator import PedestrainGenerator
from traffic_signal import TrafficSignal
from traffic_signalp import TrafficSignalP

class Simulation:
    def __init__(self, config={}):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0            # Time keeping
        self.frame_count = 0    # Frame count keeping
        self.dt = 0.01          # Simulation time step
        
        self.roads = []         # Array to store roads
        self.roadsp = []

        self.generators = []
        self.traffic_signals = []

        self.generatorsp = []
        self.traffic_signalsp = []

    def create_road(self, start, end):
        road = Road(start, end)
        self.roads.append(road)
        return road

    def create_roadp(self, start, end):
        roadp = RoadP(start, end)
        self.roadsp.append(roadp)
        return roadp    
    
    def create_roads(self, road_list):
        for road in road_list:
            self.create_road(*road)

    def create_roadsp(self, roadp_list):
        for roadp in roadp_list:
            self.create_roadp(*roadp)

    def create_gen(self, config={}):
        gen = VehicleGenerator(self, config)
        self.generators.append(gen)
        return gen

    def create_signal(self, roads, config={}):
        roads = [[self.roads[i] for i in road_group] for road_group in roads]
        sig = TrafficSignal(roads, config)
        self.traffic_signals.append(sig)
        return sig

    def create_genp(self, config={}):
        genp = PedestrainGenerator(self, config)
        self.generatorsp.append(genp)
        return genp

    def create_signalp(self, roadsp, config={}):
        roadsp = [[self.roadsp[i] for i in road_groupp] for road_groupp in roadsp]
        sigp = TrafficSignalP(roadsp, config)
        self.traffic_signalsp.append(sigp)
        return sigp

    def update(self):
        # Update every road and pedestrain road
        for road in self.roads:
            road.update(self.dt)
        
        for roadp in self.roadsp:
            roadp.update(self.dt)

        # Add vehicles
        for gen in self.generators:
            gen.update()

        for signal in self.traffic_signals:
            signal.update(self)

        for genp in self.generatorsp:
            genp.update()

        for signalp in self.traffic_signalsp:
            signalp.update(self)

        # Check roads for out of bounds vehicle
        for road in self.roads:
            # If road has no vehicles, continue
            if len(road.vehicles) == 0: continue
            # If not
            vehicle = road.vehicles[0]
            # If first vehicle is out of road bounds
            if vehicle.x >= road.length:
                # If vehicle has a next road
                if vehicle.current_road_index + 1 < len(vehicle.path):
                    # Update current road to next road
                    vehicle.current_road_index += 1
                    # Create a copy and reset some vehicle properties
                    new_vehicle = deepcopy(vehicle)
                    new_vehicle.x = 0
                    # Add it to the next road
                    next_road_index = vehicle.path[vehicle.current_road_index]
                    self.roads[next_road_index].vehicles.append(new_vehicle)
                # In all cases, remove it from its road
                road.vehicles.popleft() 


        # Check roads for out of bounds pedestrain
        for roadp in self.roadsp:
            # If road has no vehicles, continue
            if len(roadp.pedestrains) == 0: continue
            # If not
            pedestrain = roadp.pedestrains[0]
            # If first pedestrain is out of road bounds
            if pedestrain.x >= roadp.length:
                # If pedestrain has a next road
                if pedestrain.current_road_index + 1 < len(pedestrain.path):
                    # Update current road to next road
                    pedestrain.current_road_index += 1
                    # Create a copy and reset some pedestrain properties
                    new_pedestrain = deepcopy(pedestrain)
                    new_pedestrain.x = 0
                    # Add it to the next road
                    next_road_indexp = pedestrain.path[pedestrain.current_road_index]
                    self.roadsp[next_road_indexp].pedestrains.append(new_pedestrain)
                # In all cases, remove it from its road
                roadp.pedestrains.popleft() 

        # Increment time
        self.t += self.dt
        self.frame_count += 1

    def run(self, steps):
        for _ in range(steps):
            self.update()