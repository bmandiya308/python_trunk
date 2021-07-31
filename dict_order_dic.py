# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict
import string

print("This is a Dict:\n")

dict_1 =list(range(26))
dict_2 = list(string.ascii_lowercase)

d = {dict_1[i]:dict_2[i] for i in range(len(dict_1))}

for key, value in d.items():
    print(key,value)



print("\nThis is an Ordered Dict:\n")
od = OrderedDict(d)

for key, value in od.items():
    print(key, value)

