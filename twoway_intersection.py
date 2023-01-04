import numpy as np
from simulation import Simulation
from curve import turn_road
from window import Window

sim = Simulation()

# Play with these
n = 15
a = 2
b = 12
l = 300

ap = 20
bp = 3

TURN_LEFT = 0
TURN_RIGHT = 1

# Nodes
WEST_RIGHT_START = (-b-l, a)
WEST_LEFT_START =	(-b-l, -a)

SOUTH_RIGHT_START = (a, b+l)
SOUTH_LEFT_START = (-a, b+l)

EAST_RIGHT_START = (b+l, -a)
EAST_LEFT_START = (b+l, a)

NORTH_RIGHT_START = (-a, -b-l)
NORTH_LEFT_START = (a, -b-l)

# Nodes
WEST_RIGHT_STARTP = (-bp-l, ap)
WEST_LEFT_STARTP =	(-bp-l, -ap)

SOUTH_RIGHT_STARTP = (ap, bp+l)
SOUTH_LEFT_STARTP = (-ap, bp+l)

EAST_RIGHT_STARTP = (bp+l, -ap)
EAST_LEFT_STARTP = (bp+l, ap)

NORTH_RIGHT_STARTP = (-ap, -bp-l)
NORTH_LEFT_STARTP = (ap, -bp-l)


WEST_RIGHTP = (-bp, ap)
WEST_LEFTP=	(-bp, -ap)

SOUTH_RIGHTP = (ap, bp)
SOUTH_LEFTP = (-ap, bp)

EAST_RIGHTP = (bp, -ap)
EAST_LEFTP = (bp, ap)

NORTH_RIGHTP = (-ap, -bp)
NORTH_LEFTP = (ap, -bp)




WEST_RIGHT = (-b, a)
WEST_LEFT =	(-b, -a)

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)

EAST_RIGHT = (b, -a)
EAST_LEFT = (b, a)

NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)

# Roads
WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
WEST_INBOUNDP = (WEST_RIGHT_STARTP, WEST_RIGHTP)

SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
SOUTH_INBOUNDP = (SOUTH_RIGHT_STARTP, SOUTH_RIGHTP)

EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
EAST_INBOUNDP = (EAST_RIGHT_STARTP, EAST_RIGHTP)

NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)
NORTH_INBOUNDP = (NORTH_RIGHT_STARTP, NORTH_RIGHTP)

WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_START)
WEST_OUTBOUNDP = (WEST_LEFTP, WEST_LEFT_STARTP)

SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_START)
SOUTH_OUTBOUNDP = (SOUTH_LEFTP, SOUTH_LEFT_STARTP)

EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_START)
EAST_OUTBOUNDP = (EAST_LEFTP, EAST_LEFT_STARTP)

NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_START)
NORTH_OUTBOUNDP = (NORTH_LEFTP, NORTH_LEFT_STARTP)


WEST_STRAIGHT = (WEST_RIGHT, EAST_LEFT)
SOUTH_STRAIGHT = (SOUTH_RIGHT, NORTH_LEFT)
EAST_STRAIGHT = (EAST_RIGHT, WEST_LEFT)
NORTH_STRAIGHT = (NORTH_RIGHT, SOUTH_LEFT)

WEST_STRAIGHTP = (WEST_RIGHTP, EAST_LEFTP)
SOUTH_STRAIGHTP = (SOUTH_RIGHTP, NORTH_LEFTP)
EAST_STRAIGHTP = (EAST_RIGHTP, WEST_LEFTP)
NORTH_STRAIGHTP = (NORTH_RIGHTP, SOUTH_LEFTP)

WEST_RIGHT_TURN = turn_road(WEST_RIGHT, SOUTH_LEFT, TURN_RIGHT, n)
WEST_LEFT_TURN = turn_road(WEST_RIGHT, NORTH_LEFT, TURN_LEFT, n)

SOUTH_RIGHT_TURN = turn_road(SOUTH_RIGHT, EAST_LEFT, TURN_RIGHT, n)
SOUTH_LEFT_TURN = turn_road(SOUTH_RIGHT, WEST_LEFT, TURN_LEFT, n)

EAST_RIGHT_TURN = turn_road(EAST_RIGHT, NORTH_LEFT, TURN_RIGHT, n)
EAST_LEFT_TURN = turn_road(EAST_RIGHT, SOUTH_LEFT, TURN_LEFT, n)

NORTH_RIGHT_TURN = turn_road(NORTH_RIGHT, WEST_LEFT, TURN_RIGHT, n)
NORTH_LEFT_TURN = turn_road(NORTH_RIGHT, EAST_LEFT, TURN_LEFT, n)

sim.create_roads([
    WEST_INBOUND,
    SOUTH_INBOUND,
    EAST_INBOUND,
    NORTH_INBOUND,

    WEST_OUTBOUND,
    SOUTH_OUTBOUND,
    EAST_OUTBOUND,
    NORTH_OUTBOUND,

    WEST_STRAIGHT,
    SOUTH_STRAIGHT,
    EAST_STRAIGHT,
    NORTH_STRAIGHT,

    *WEST_RIGHT_TURN,
    *WEST_LEFT_TURN,

    *SOUTH_RIGHT_TURN,
    *SOUTH_LEFT_TURN,

    *EAST_RIGHT_TURN,
    *EAST_LEFT_TURN,

    *NORTH_RIGHT_TURN,
    *NORTH_LEFT_TURN
])

sim.create_roadsp([
    WEST_INBOUNDP,
    SOUTH_INBOUNDP,
    EAST_INBOUNDP,
    NORTH_INBOUNDP,

    WEST_OUTBOUNDP,
    SOUTH_OUTBOUNDP,
    EAST_OUTBOUNDP,
    NORTH_OUTBOUNDP,

    WEST_STRAIGHTP,
    SOUTH_STRAIGHTP,
    EAST_STRAIGHTP,
    NORTH_STRAIGHTP
])

def road(a): return range(a, a+n)
def roadp(ap): return range(ap, ap+n)

sim.create_gen({
'vehicle_rate': 100,
'vehicles':[
    [3, {'path': [0, 8, 6]}],
    [1, {'path': [0, *road(12), 5]}],
    [1, {'path': [0, *road(12+n), 7]}],

    [3, {'path': [1, 9, 7]}],
    [1, {'path': [1, *road(12+2*n), 6]}],
    [1, {'path': [1, *road(12+3*n), 4]}],


    [3, {'path': [2, 10, 4]}],
    [1, {'path': [2, *road(12+4*n), 7]}],
    [1, {'path': [2, *road(12+5*n), 5]}],

    [3, {'path': [3, 11, 5]}],
    [1, {'path': [3, *road(12+6*n), 4]}],
    [1, {'path': [3, *road(12+7*n), 6]}]
]})


sim.create_genp({
'pedestrain_rate' : 50,
'pedestrains':[
    [3, {'path': [0, 8, 6]}],
    [3, {'path': [1, 9, 7]}],
    [3, {'path': [2, 10, 4]}],
    [3, {'path': [3, 11, 5]}],
]})

sim.create_signal([[0, 2], [1, 3]])

sim.create_signalp([[0, 2], [1, 3]])


# Start simulation
win = Window(sim)
win.zoom = 5
win.run(steps_per_update=10)