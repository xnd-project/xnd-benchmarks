
# XND compared with NumPy.


## Data conversion from Python values

Sometimes data is naturally in Python object form, for example when using Python's JSON module. This benchmark compares reading a list of int64 values. XND is faster both for type inference and if a dtype is given. The fastest possible way for XND is to read data with a schema-like full type:

```
$ python data_conversion_int64.py

Type inference
--------------

   xnd: 0.21521806716918945
   numpy: 0.4042797088623047

Dtype provided
--------------

   xnd:   0.17266035079956055
   numpy: 0.4040689468383789

Full type provided
-------------------

   xnd:   0.10901474952697754
```


This benchmark compares reading a list of tuples, the example is from the NumPy documentation. NumPy is omitted from the type inference section since it infers the "O" python object type:


```
$ python data_conversion_tuple.py 

Type inference
---------------

xnd:   0.9455676078796387

Dtype provided
--------------

xnd:   1.0472655296325684
numpy: 1.2794170379638672

Full type provided
-------------------

xnd:   0.7372479438781738
```
