'''TASK 1'''
import matplotlib
import numpy as np 
import pylab
import matplotlib.pyplot as plt 
import math
import random

def Randwalk(n, start):

    x = 0
    y = start

    time = [x]
    position = [y] 

    for i in range (1,n+1):

        move = np.random.uniform(0.0,1.0)

        if move < 0.75:  #up  
            x += 1
            y += np.random.uniform(0.0,1.0)  

        elif move > 0.25:   #down
            x += 1
            y += -(np.random.uniform(0.0,1.0))
        
        else: #not going anywhere
            x +=1

        time.append(x)
        position.append(y)

    
    return [time, position], position

start = 0
lst = []

for i in range (10000):
    a,arr  = Randwalk(1000, start)
    d = arr[-1] - start 
    lst.append(d)

print(sum(lst)/len(lst))
plt.xlabel('displacement covered from starting point')
plt.ylabel('frequency')
plt.hist(lst, bins=10)

plt.show()

plt.xlabel('Time')
plt.ylabel('Position')
plt.plot(a[0],a[1],'r-', label = "Randwalk1")

plt.show()