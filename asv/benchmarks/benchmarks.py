# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import xnd
import numpy as np


class DataConversionSuite:
    params = [
        [10 ** n for n in range(7)],
        ['float64', 'int64', 'tuple'],
        ['full', 'partial', 'none'],
        ['xnd', 'np'],
    ]
    param_names = ['size', 'dtype', 'type_info', 'module']

    def setup(self, size, dtype, type_info, module):
        if 'int' in dtype:
            self.lst = [1] * size
        elif 'float' in dtype:
            self.lst = [1.0] * size
        elif dtype == 'tuple':
            self.lst = [('Rex', 9, 81.0)] * size
            if module == 'np':
                dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
            elif module == 'xnd':
                dtype = "(fixed_string(10), int32, float32)"
        self.function = globals()[module].array

        if type_info == 'full':
            self.kwargs = {'type': f'{size} * {dtype}'}
            if module == 'np':
                raise NotImplementedError
        elif type_info == 'partial':
            self.kwargs = {'dtype': dtype}
        elif type_info == 'none':
            self.kwargs = {}

    def time_create(self, size, dtype, type_info, module):
        self.function(self.lst, **self.kwargs)


class DataAccessSuite:
    params = [
        [10 ** n for n in range(7)],
        [(x, y) for x in range(1, 4) for y in range(1, 4) if x >= y],
        ['xnd', 'np'],
    ]
    param_names = ['size', 'dim', 'module']

    def setup(self, size, dim, module):
        ndim = dim[0]
        size_per_dim = int(size ** (1/ndim))
        shape = (size_per_dim,) * ndim
        lst = 1
        for i in range(ndim):
            lst = [lst] * size_per_dim

        self.array = globals()[module].array(lst)

    def time_access_tuple(self, size, dim, module):
        self.array[(0,) * dim[1]]

    def time_access_chained(self, size, dim, module):
        a = self.array
        for i in range(dim[1]):
            a = a[0]
