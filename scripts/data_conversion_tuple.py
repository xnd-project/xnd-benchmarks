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

### List of structured dtypes, from the numpy documentation ###
lst = [('Rex', 9, 81.0)] * 10000000

# Infer the type. This is only possible in xnd, NumPy infers a Python object type.
print("\nType inference")
print("---------------\n")
start = time()
x = xnd.array(lst)
stop = time()
print("xnd:  ", stop-start)


# Dtype is provided.
print("\nDtype provided")
print("--------------\n")
start = time()
x = xnd.array(lst, dtype="(fixed_string(10), int32, float32)")
stop = time()
print("xnd:  ", stop-start)
del x

dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
start = time()
x = np.array(lst, dtype=dt)
stop = time()
print("numpy:", stop-start)
del x

# Full type with the array size is provided, only possible in xnd.
print("\nFull type provided")
print("-------------------\n")
start = time()
x = xnd.array(lst, type="10000000 * (fixed_string(10), int32, float32)")
stop = time()
print("xnd:  ", stop-start)
print("\n")
del x, lst
