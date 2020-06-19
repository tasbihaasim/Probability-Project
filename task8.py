import math
import random
import numpy as np
import pylab
from collections import OrderedDict 
import matplotlib.pyplot as plt


class RandomWalk:

    def __init__(self, l, R, seed=1000):

        self.l = l
        self.R = R

        self.seed = seed

        self.max_steps = 1000
    
        self.x = None
        self.y = None



    def walk(self):

        # set the initial position to be the origin
        x_0 = np.random.uniform(0.0, 100.0)
        y_0 = np.random.uniform(-math.sqrt(100.0**2-x_0**2), math.sqrt(100.0**2-x_0**2))
 

        x = []
        y = []

        random.seed(self.seed)

        for n in range(self.max_steps):

            # compute a random angle
            angle = np.random.uniform(0, 2*math.pi) # A single value
            # print("angle: ", angle)

            # length of single step
            l = np.random.uniform(0.0,1.0) # A single value
            # print("step: ", l)


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

        return x,y
            

def random_walk():

    # length of single step
    l = 1.0
    # print("step: ", l)

    # maximum radius of domain
    R = 100.0

    # # take steps, draw a segment in a random direction, and save the frame
    pylab.clf()

    # # draw a circle to indicate the extent of the domain
    npts = 360
    theta = np.arange(npts)*2*math.pi/(npts-1)

    pylab.plot(R*np.cos(theta), R*np.sin(theta), color='k')

    pylab.subplots_adjust(left=0,right=1.0,bottom=0,top=1.0)
    dis = []
    dict = {}
    # do a random walk
    lst = []
    for i in range(1):
        r1 = RandomWalk(l, R, seed=1000)
        r2 = RandomWalk(l, R, seed=1000)
        r1_x, r1_y = r1.walk()
        r2_x, r2_y = r2.walk()
        
    
        num = 0 
        dis.append(math.sqrt((r1_x[0] - r2_x[0])**2 + (r1_y[0] - r2_y[0])**2))
        while num < len(r1_x):
            if math.sqrt((r1_x[num] - r2_x[num])**2 + (r1_y[num] - r2_y[num])**2) < 1:
                lst.append(num)
                if num not in dict:
                    dict[num] = 1
                else:
                    dict[num] += 1
            num += 1
    final = []
    

    dict1 = OrderedDict(sorted(dict.items()))
    for key,value in dict1.items():
        final.append((key, value))


    x_val = [x[0] for x in final]
    y_val = [x[1] for x in final]
    plt.plot(x_val,y_val)
    # plt.scatter(x_val,y_val)
##    plt.show()
    plt.xlabel('Steps at which they are within 1 unit')
    plt.ylabel('Frequency')
    plt.hist(lst, bins=10)
    plt.show()
    print(sum(lst)/len(lst))


##    for n in range(len(r1.x)-1):
##                
##        pylab.plot([r1.x[n], r1.x[n+1]], 
##                   [r1.y[n], r1.y[n+1]], color='r')
##
##        pylab.plot([r2.x[n], r2.x[n+1]], 
##                   [r2.y[n], r2.y[n+1]], color='b')
##
##        pylab.axis([-1.1*R,1.1*R,-1.1*R,1.1*R])
##
##        pylab.axis("off")
##
##        f = pylab.gcf()
##        f.set_size_inches(7.2*2, 7.2*2)
##
##        pylab.savefig(r"C:\Users\USER\Desktop\probproject\task8walk\random_walk_%04d.png" % n)



if __name__== "__main__":
    random_walk()
