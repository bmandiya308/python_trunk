#print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))

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
#print(functools.reduce(operator.add,zip(lst1,lst2)))
for i in list(functools.reduce(lambda x,y: x+y,zip(lst1,lst2))):
    print(i)


print(list(reduce(lambda x,y:x+y,zip(lst1,lst1))))