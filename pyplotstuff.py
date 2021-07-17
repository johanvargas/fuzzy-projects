from matplotlib import pyplot as plt
import numpy as np
import math
import sys

#a = float(sys.argv[1])
#b = int(sys.argv[2])

a = 23
b  = 34
# X
x = np.arange(-100, 100)

# Expression 1
y = ((a * x) - b)

# Expression 2
b = ((0.5 * x) + 3)


# Expression 3, circle
# x^2 + y^2 = r^2


plt.plot(x,y, label = 'Negative Slope')
plt.plot(x, b, label = 'Positive Slope')
plt.plot(x, x, label = 'dummy')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Linear System')
plt.legend()

plt.show()
