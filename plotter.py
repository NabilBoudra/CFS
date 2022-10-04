from lib2to3.pytree import convert
from contestant import convertToActual
import matplotlib.pyplot as plt
def plot(speed): 
    xAxis=[]
    yAxis=[]
    for i in range(len(speed)):
        if speed[i] != -1 : 
            xAxis.append(convertToActual(i))
            yAxis.append(speed[i]) 
    plt.plot(xAxis,yAxis) 
    plt.savefig('img.png')
