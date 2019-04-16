import xnd
import numpy as np
from time import time


repeat = 1000000


### Small array ###
lst = [[1,2,3], [3,4,5]]

print("\nAccessing an element in a small array")
print("-------------------------------------\n")
x = xnd.array(lst)
start = time()
for i in range(repeat):
    y = x[1][2]
stop = time()
print("   xnd:  ", stop-start)
del x, y

start = time()
x = np.array(lst)
for i in range(repeat):
    y = x[1][2]
stop = time()
print("   numpy:", stop-start)
del x, y


### Medium sized array ###
print("\nAccessing an element in a medium sized array")
print("--------------------------------------------\n")
lst = 10 * [100 * [1000 * [1]]]

x = xnd.array(lst)
start = time()
for i in range(repeat):
    y = x[8][99][1]
stop = time()
print("   xnd:  ", stop-start)
del x, y

start = time()
x = np.array(lst)
for i in range(repeat):
    y = x[8][99][1]
stop = time()
print("   numpy:", stop-start)
del x, y


### Element in an array of tuples ###
lst = [('Rex', 9, 81.0)] * 10000000

print("\nAccessing an element in an array of tuples")
print("------------------------------------------\n")
x = xnd.array(lst, dtype="(fixed_string(10), int32, float32)")
start = time()
for i in range(repeat):
    y = x[701299][0]
stop = time()
print("   xnd:  ", stop-start)
del x

dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
x = np.array(lst, dtype=dt)
start = time()
for i in range(repeat):
    y = x[701299][0]
stop = time()
print("   numpy:", stop-start)
del x
