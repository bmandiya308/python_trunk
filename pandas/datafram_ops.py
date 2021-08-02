import pandas as pd
import numpy as np
import matplotlib
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
print(d)
df = pd.DataFrame(d)
print(df)

print("With Index")
print(pd.DataFrame(d, index=['d', 'b', 'a']))

print("With Index and column")
print(pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']))

print(df.index)
print(df.columns)
print(df.one)
print(df.two)

print("From dict of ndarrays / lists")

d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}
print(pd.DataFrame(d))
print(pd.DataFrame(d, index=['a', 'b', 'c', 'd']))

print("From structured or record array¶")

data = np.zeros((2, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
print(pd.DataFrame(data))
print(pd.DataFrame(data, index=['first', 'second']))
print(pd.DataFrame(data, columns=['C', 'A', 'B']))

print("From a list of dicts¶")
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print(pd.DataFrame(data2))
print(pd.DataFrame(data2, index=['first', 'second']))
print(pd.DataFrame(data2, columns=['a', 'b']))

print("From a dict of tuples¶")

df = pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
               ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
               ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
               ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
               ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
print(df)

print("DataFrame.from_dict takes a dict of dicts or a dict of array-like sequences and returns a DataFrame")
print(pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])])))
print(pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),orient='index', columns=['one', 'two', 'three']))

print("DataFrame.from_records takes a list of tuples or an ndarray with structured dtype")
print(data)
print(pd.DataFrame.from_records(data, index='C'))

print("Column selection, addition, deletion¶")
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df['one'])
print(df)
print("after delete")
del df['two']
print(df)
df['foo'] = 'bar'
print(df)
df['one_trunc'] = df['one'][:2]
print(df)
df.insert(1, 'bar', df['one'])
print(df)

print("Assigning new columns in method chains¶")
iris = pd.read_csv('D:\\xls_to_csv\cus_data.csv')
print(iris.head())
print(iris.assign(sepal_ratio=iris['Customerid'] / iris['Pin']).head())
print("We can also pass in a function of one argument to be evaluated on the DataFrame being assigned to.")
print(iris.assign(sepal_ratio=lambda x: (x['Customerid'] / x['Customerid'])).head())
print(iris.query('Customerid > 200000').assign(new_col = iris['Customerid'] / iris['Customerid']).head())
print(iris.query('Customerid > 200000').assign(SepalRatio=lambda x: x.Pin / 100,PetalRatio=lambda x: x.Pin / 10).plot(kind='scatter', x='SepalRatio', y='PetalRatio'))

dfa = pd.DataFrame({"A": [1, 2, 3],
                    "B": [4, 5, 6]})

df_new = dfa.assign(C=lambda x: x['A'] + x['B'],
                    D=lambda x: x['A'] + x['C'])
print(df_new)

print("Data alignment and arithmetic¶")
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
print("DF :\n",df)
print("DF2 :\n",df2)
print("DF + DF2 :\n",df + df2)

print("df - df.iloc[0] :\n",df - df.iloc[0])

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=list('ABC'))
print(df)
print(type(df['A']))
print(df - df['A'])

print("Original :\n",df)
print("Added :\n",df * 5 + 2)
print("1 / df :\n",1 / df)
print("df ** 4 : \n",df ** 4)

print("Boolean operators work as well:")

df1 = pd.DataFrame({'a': [1, 0, 1], 'b': [0, 1, 1]}, dtype=bool)
df2 = pd.DataFrame({'a': [0, 1, 1], 'b': [1, 1, 0]}, dtype=bool)
print("df1 :\n",df1)
print("df2 :\n",df2)
print("df1 & df2 :\n",df1 & df2)
print("df1 | df2 :\n",df1 | df2)
print("df1 ^ df2 :\n",df1 ^ df2)
print("-df1 :\n",-df1)


print("Transposing")
print(df)
print("Only show first 5 rows :\n")
print(df[:5].T)

print("DataFrame interoperability with NumPy functions¶")
print("Orioginal :\n",df)
print("np.exp(df) : \n",np.exp(df))
print("np.asarray(df) :\n",np.asarray(df))

print("The ufunc is applied to the underlying array in a Series.")
ser = pd.Series([1, 2, 3, 4])
print("Original : \n",ser)
print("np.exp(ser) :\n",np.exp(ser))

print("using numpy.remainder() on two Series with differently ordered labels will align before the operation.")
ser1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
ser2 = pd.Series([1, 3, 5], index=['b', 'a', 'c'])
print("ser1 :\n",ser1)
print("ser2 :\n",ser2)
print(" np.remainder(ser1, ser2) :\n", np.remainder(ser1, ser2))
ser3 = pd.Series([2, 4, 6], index=['b', 'c', 'd'])
print("ser3 :\n",ser3)
print("np.remainder(ser1, ser3) :\n",np.remainder(ser1, ser3))

ser = pd.Series([1, 2, 3])
idx = pd.Index([4, 5, 6])
print("(np.maximum(ser, idx) :\n",np.maximum(ser, idx))
