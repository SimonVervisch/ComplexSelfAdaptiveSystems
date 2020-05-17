import matplotlib
matplotlib.use('TkAgg')
from pylab import *


# import necessary modules
# define model parameters
import random as rd
n = 1000 # number of particles
sd = 0.1 # standard deviation of Gaussian noise

def initialize():
    """
    Test
    """
    global xlist, ylist
    xlist = []
    ylist = []
    for i in xrange(n):
        xlist.append(rd.gauss(0, 1))

        ylist.append(rd.gauss(0, 1))


def observe():
    global xlist, ylist
    cla()
    plot(xlist,ylist, '.')
    # visualize system states

def update():
    global xlist, ylist
    for i in xrange(n):
        xlist[i] += rd.gauss(0, sd)
        ylist[i] += rd.gauss(0, sd)
    # update system states for one discrete time step


import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
