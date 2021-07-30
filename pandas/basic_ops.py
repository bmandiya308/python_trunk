import numpy as np
import pandas as pd
#one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).
#s = pd.Series(data, index=index)

'''
Here, data can be many different things:
a Python dict
an ndarray
a scalar value (like 5)
'''
print("LIST :")
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s['a'])
for i in s:
    print(i)

print(s.index)
print(pd.Series(np.random.randn(5)))

print("DICTIONARY :")
d = {'b': 1, 'a': 0, 'c': 2}
df = pd.Series(d)
print(df['b'])
print(df)
df_1 = pd.Series(d, index=['b', 'c', 'd', 'a'])
print(df_1)
print(df_1['d'])
#print(df_1['f'])   give key error
print("Dictionary get :")
print(df_1.get('a',np.nan))
print(df_1.get('f',np.nan))
if('a' in df_1):
    print("Yes a is there")
if(1 in df_1):  #Not Working
    print("Yes 1 is there")

if('e' not in df_1):
    print("Yes e is Not there")

if(df_1['d'] is np.nan):   #Not Working
    print("yes its None")

print("SCALAR :")
df_2 = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
print(df_2)
print(df_2.dtype)
print(df_2.array)
print(df_2.to_numpy(dtype=int))

print("Vectorized operations and label alignment with Series")
print("Actaul")
print(s)
print("Addition")
print(s + s)
print("Multiplication")
print(s * 2)
print("Exponent")
print(np.exp(s))

print("Actual")
print(s)
print("Operation")
print(s[1:] + s[:-1])
print(s[0:] + s[:-1])

print("Series can also have a name attribute:")
s = pd.Series(np.random.randn(5), name='something')
print(s)
print(s.name)
s2 = s.rename("different")
print(s2)
print(s2.name)

