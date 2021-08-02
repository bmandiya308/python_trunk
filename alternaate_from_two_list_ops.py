print("Using Normal procedure")
list_1 = [1,2,3,4,5,6,7]
list_2 = [-1,-2,-3,-4,-5,-6,-7]
list_3 = list()
for i in list_1:
    list_3.append(i)
    for j in list_2:
        list_3.append(j)
        list_2.remove(j)
        break
print("First List :\n",list_1)
print("Second List :\n",list_2)
print("Conbined List :\n",list_3)

print("Using comprehension")

list_1 = [1,2,3,4,5,6,7]
list_2 = [-1,-2,-3,-4,-5,-6,-7]
list_4 = [sub[i] for i in (range(len(list_1))) for sub in [list_1,list_2]]
print(list_4)

print("Using Zip")
list_5 = list(zip(list_1,list_2)) #[(1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)]
print(list_5)

print("Python3 program to merge two lists")
# alternatively

def countList(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
                      for sub in [lst1, lst2]]
# Driver code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(countList(lst1, lst2))

print("Using reduce")
# Python3 program to merge two lists
# alternatively
import operator
from functools import reduce

def countList(lst1, lst2):
    return reduce(operator.add, zip(lst1, lst2))

# Driver code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print("Reduce")
print(list(countList(lst1, lst2)))
print("Reduce")
import functools
print(functools.reduce(operator.add,zip(list_1,list_2)))
for i in list(functools.reduce(lambda x,y: x+y,zip(list_1,list_2))):
    print(i)


print("Using NumPy")

# Python3 program to merge two lists
# alternatively
#import numpy as np

# def countList(lst1, lst2):
#     return np.array([[i, j] for i, j in zip(lst1, lst2)]).ravel()
#
# # Driver code
# lst1 = [1, 2, 3]
# lst2 = ['a', 'b', 'c']
# print(countList(lst1, lst2))

print("testing")
final_list =[]
list_1 = [1,2,3,4,5,6,7]
list_2 = [-1,-2,-3,-4,-5,-6,-7]

print(reduce(operator.add,zip(list_1,list_2)))


