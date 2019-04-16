import xnd
import numpy as np
from time import time


repeat = 1000000

### Small array view ###
lst = [[1,2,3], [3,4,5]]

print("\nSmall subarray view")
print("-------------------\n")
x = xnd.array(lst)
start = time()
for i in range(repeat):
    y = x[1]
stop = time()
print("   xnd:  ", stop-start)
del x, y

start = time()
x = np.array(lst)
for i in range(repeat):
    y = x[1]
stop = time()
print("   numpy:", stop-start)
del x, y


### Medium sized array view ###
print("\nMedium sized subarray view")
print("--------------------------\n")
lst = 10 * [100 * [1000 * [1]]]

x = xnd.array(lst)
start = time()
for i in range(repeat):
    y = x[8][99]
stop = time()
print("   xnd:  ", stop-start)
del x, y

start = time()
x = np.array(lst)
for i in range(repeat):
    y = x[8][99]
stop = time()
print("   numpy:", stop-start)
del x, y
