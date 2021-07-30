'''
NumPy is a Python package. It stands for 'Numerical Python'. It is a library consisting of multidimensional array objects
and a collection of routines for processing of array.
'''
import numpy as np

#N-dimensional array

a = np.array([1,2,3])
print(a)

# more than one dimensions
a = np.array([[1, 2], [3, 4]])
print(a)

# minimum dimensions
a = np.array([1, 2, 3,4,5], ndmin = 2)
print(a)
a = np.array([1, 2, 3,4,5], ndmin = 3)   #[[[arr iterm]]]
print(a)

# dtype parameter
'''
'b' − boolean
'i' − (signed) integer
'u' − unsigned integer
'f' − floating-point
'c' − complex-floating point
'm' − timedelta
'M' − datetime
'O' − (Python) objects
'S', 'a' − (byte-)string
'U' − Unicode
'V' − raw data (void)
'''

a = np.array([1, 2, 3], dtype = complex)
print(a)
'''
for i in a:
    print(i)
'''

#dtype datatype

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a['age'])


#Arr shape

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)

a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(a)
print(b)

a = np.arange(24)
print (a)

#Multidiemtional
a = np.arange(24)
a.ndim
# now reshape it
b = a.reshape(2,4,3)
print(b)


#item Size

# dtype of array is int8 (1 byte)
x = np.array([1,2,3,4,5], dtype = np.int8)
print(x.itemsize)  #1

x = np.array([1,2,3,4,5], dtype = np.float32)
print(x.itemsize) #4

#currentvalues of flag
x = np.array([1,2,3,4,5])
print(x.flags)

#empty array
x = np.empty([3,2], dtype = int)
print(x)

# array of five zeros. Default dtype is float
x = np.zeros(5)
print(x)
x = np.zeros((5,), dtype = np.int)
print(x)
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(x)

# array of five ones. Default dtype is float
x = np.ones(5)
print(x)
x = np.ones([2,2], dtype = int)
print(x)

# convert list to ndarray
x = [1,2,3]
a = np.asarray(x)
print(a)

# dtype is set
x = [1,2,3]
a = np.asarray(x, dtype = float)
print(a)

# ndarray from tuple
x = (1,2,3)
a = np.asarray(x)
print(a)


# ndarray from list of tuples
x = [(1,2,3),(4,5)]
a = np.asarray(x)
print(a)

'''
s = "Hello World"
a = np.frombuffer(s, dtype = 'S1')
print(a)
'''

# create list object using range function
list = range(5)
print(list)

# obtain iterator object from list
list = range(5)
it = iter(list)
# use iterator to create ndarray
x = np.fromiter(it, dtype = float)
print(x)

print("arange")
x = np.arange(5)
print(x)

# dtype set
x = np.arange(5, dtype = float)
print(x)

# start and stop parameters set
x = np.arange(10,20,2)
print(x)

x = np.linspace(10,20,5)
print(x)

# endpoint set to false
x = np.linspace(10,20, 5, endpoint = False)
print(x)

# find retstep value
x = np.linspace(1,2,5, retstep = True)
print(x)


# default base is 10
a = np.logspace(1.0, 2.0, num = 10)
print(a)

# set base of log space to 2
a = np.logspace(1,10,num = 10, base = 2)
print(a)

# slice items starting from index
a = np.arange(10)
print(a[2:])

# slice items between indexes
a = np.arange(10)
print(a[2:5])


x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

print('Our array is:')
print(x)
print('\n')

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]

print('The corner elements of this array are:')
print(y)

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)

# slice items starting from index
print('Now we will slice the array from the index a[1:]')
print(a[1:])


a = np.array([[1,2,3],[3,4,5],[4,5,6]])

print('Our array is:')
print(a)
print('\n')

# this returns array of items in the second column
print('The items in the second column are:')
print(a[...,1])
print('\n')

# Now we will slice all items from the second row
print('The items in the second row are:')
print(a[1,...])
print('\n')

# Now we will slice all items from column 1 onwards
print('The items column 1 onwards are:')
print(a[...,1:])


x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

print('Our array is:')
print(x)
print('\n')

# slicing
z = x[1:4,1:3]

print('After slicing, our array becomes:')
print(z)
print('\n')

# using advanced index for column
y = x[1:4,[1,2]]

print('Slicing using advanced index for column:')
print(y)


x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

print('Our array is:')
print(x)
print('\n')

# Now we will print the items greater than 5
print('The items greater than 5 are:')
print(x[x > 5])

a = np.array([np.nan, 1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])

a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)])

#broadcasting
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print(c)


a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])

print('First array:')
print(a)
print('\n')

print('Second array:')
print(b)
print('\n')

print('First Array + Second Array')
print(a + b)


#iteratinon over array

a = np.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is:')
print(a)
print('\n')

print('Modified array is:')
for x in np.nditer(a):
   print(x,)
