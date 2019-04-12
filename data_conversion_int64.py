import xnd
import numpy as np
from time import time


# ========================================================================
#                          Python data conversion
# ========================================================================

#
# Timeit is too slow for large arrays, so this benchmark just uses time.time(),
# which is accurate enough for this purpose.
#


### List of int64_t values ###
lst = [1] * 10000000

# Type inference for reading a medium sized Python list.
print("\nType inference")
print("--------------\n")
start = time()
x = xnd.array(lst)
stop = time()
print("   xnd:  ", stop-start)
del x

start = time()
x = np.array(lst)
stop = time()
print("   numpy:", stop-start)
del x


# The same, but with an explicit dtype.
print("\nDtype provided")
print("--------------\n")
start = time()
x = xnd.array(lst, dtype="int64")
stop = time()
print("   xnd:  ", stop-start)
del x

start = time()
x = np.array(lst, dtype="int64")
stop = time()
print("   numpy:", stop-start)
del x


# The same, but with a full type that includes the array size. This is
# only possible in xnd.
print("\nFull type provided")
print("-------------------\n")
start = time()
x = xnd.array(lst, type="10000000 * int64")
stop = time()
print("   xnd:  ", stop-start)
del x
print("\n")
