tuple_a = tuple(range(1,12))
print(tuple_a)
print("count")
print(tuple_a.count(10))
print("index")
print(tuple_a.index(11))

print("remove elements")
list_b = list(tuple_a)
list_b.remove(5)
del list_b[1:3]
tuple_b = tuple(list_b)
print(tuple_b)
tuple_b = tuple()
print(tuple_b)
