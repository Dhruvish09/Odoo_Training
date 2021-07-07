# 14). Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.


import random

x = random.randrange(100, 200, 5)
print(x)

import numpy as np
from numpy.core.fromnumeric import size
x = np.random.randint(low=100, high=200, size=5)
print(x)
