'''TASK 2'''
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
        if move < 0.95:  #up  
            x += 1
            y += 1  
        elif move > 0.05:   #down
            x += 1
            y += -1
        else: #not going anywhere
            x +=1
        time.append(x)
        position.append(y)
    return [time,position], position

start1 = 0
start2 = 50


def task2(start1, start2, a, b): 

    time = 0
    lst = []
   
    while time < len(a): 
        if a[time]==b[time]:
            x= (time)
            lst.append(x)
        time+=1
    return lst
lst =[]

for i in range(0,1000):
    Randwalk1, a = Randwalk(1000, start1)
    Randwalk2, b = Randwalk(1000, start2)
    lst += task2(start1, start2, a, b)

plt.xlabel('Steps required to meet')
plt.ylabel('frequency')
plt.hist(lst, bins=10)
print(sum(lst)/len(lst))
plt.show()