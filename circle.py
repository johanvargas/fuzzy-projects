from matplotlib import pyplot as plt
import numpy as np
import math
import sys

n = 100 # the length of x or the size of the sample
#graph_type = lambda n: format("The Square Root of numbers 0 to {}", str(n))    
graph_type = "The sqrt of 0 - " + str(n) + "."
graph_type_2 = "Circle"

def sqrt(number):
    return math.sqrt(number)
# equation of a circle 
# x^2 + y^2 = r^2

def plot_circle(x, r = 5):
     plot_x = math.sqrt(x)
     radius = math.sqrt(r)
     return plot_x - radius

x = np.arange(n)
y = list(map(sqrt, x))
y2 = list(map(plot_circle, x))

plt.plot(x, y, label = graph_type)
plt.plot(x, y2, label = graph_type_2 )

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Circle')
plt.legend()

plt.show()

#from https://www.pythonpool.com/matplotlib-circle/
# plotting a circle

# angle = np.linspace(0, 2 * np.pi, 150)
