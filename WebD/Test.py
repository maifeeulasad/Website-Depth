import matplotlib.pyplot as plt
import numpy as np


'''
plt.ion()
for i in range(50):
    y = np.random.random([10,1])
    plt.plot(y)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

'''
plt.ion()

x=[]
y=[]

for i in range(1,5):
    x.append(i)
    y.append(i)
    plt.plot(x,y)
    plt.pause(0.1)
    plt.draw()
    plt.clf()


plt.draw()
plt.show()