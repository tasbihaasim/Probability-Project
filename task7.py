import math
import random

import numpy as np
import pylab


class RandomWalk:

    def __init__(self, l, R, seed=1000):

        self.l = l
        self.R = R

        self.seed = seed

        self.max_steps = 5000

        self.x = None
        self.y = None


    def walk(self):

        # set the initial position to be the origin
        x_0 = 0.0
        y_0 = 0.0

        x = []
        y = []

        random.seed(self.seed)

        for n in range(self.max_steps):

            # compute a random angle
            angle = np.random.uniform(0, 2*math.pi) # A single value
            print("angle: ", angle)

            # length of single step
            steps = [0, 0.5, 1]
            l = np.random.choice(steps) # A single value
            print("step: ", l)


            # compute the end coordinates of the segment
            x_1 = self.l*math.cos(angle) + x_0
            y_1 = self.l*math.sin(angle) + y_0

            x.append(x_1)
            y.append(y_1)
            
            # have we hit the edge of our domain?
            if math.sqrt(x_1**2 + y_1**2) <= self.R:
                x_0 = x_1
                y_0 = y_1

        self.x = np.array(x)
        self.y = np.array(y)
            

def random_walk():

    # length of single step
    l = 1.0

    # maximum radius of domain
    R = 100.0

    # take steps, draw a segment in a random direction, and save the frame
    pylab.clf()

    # draw a circle to indicate the extent of the domain
    npts = 360
    theta = np.arange(npts)*2*math.pi/(npts-1)

    pylab.plot(R*np.cos(theta), R*np.sin(theta), color='k')

    pylab.subplots_adjust(left=0,right=1.0,bottom=0,top=1.0)

    # do a random walk
    r1 = RandomWalk(l, R, seed=1000)
    r1.walk()

    for n in range(len(r1.x)-1):
                
        pylab.plot([r1.x[n], r1.x[n+1]], 
                   [r1.y[n], r1.y[n+1]], color='r')

        pylab.axis([-1.1*R,1.1*R,-1.1*R,1.1*R])
        pylab.axis("off")

        f = pylab.gcf()
        f.set_size_inches(7.2*2, 7.2*2)

        pylab.savefig(r"C:\Users\USER\Desktop\probproject\walk7_2\random_walk_%04d.png" % n)



if __name__== "__main__":
    random_walk()