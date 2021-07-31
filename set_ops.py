set_a = set(range(1,11))
print(set_a)

print("add item in set")
set_a.add(11)
print(set_a)
set_a.add(11)
print(set_a)

print("remove item from set")
set_a.pop() #first item remove
set_a.remove(5) #fetch error if not present
print(set_a)
set_b = set_a.copy()
set_a.discard(8) #will not give any error if any error
print(set_a)
set_a.clear()
print(set_a)
print(set_b)

print("set difference")
set_c = set_b.copy()
set_b.add(12)
set_c.add(13)
print(set_b.difference(set_c))
print(set_c.difference(set_b))
print(set_b.intersection(set_c))
print(set_c.intersection(set_b))
print(set_b.union(set_c))
print(set_c.union(set_b))
print("intersect diff update")
set_d = set_b.copy()
set_e = set_c.copy()
print(set_d)
print(set_e)
set_d.intersection_update(set_e)
print(set_d)
print(set_e)
set_e.difference_update(set_d)
print(set_d)
print(set_e)

print("update set")
set_e.update(set_d)
print(set_d)
print(set_e)

set_d.add(12)
print("symentric diff") #compare both side available or not
print("before")
print(set_d.symmetric_difference(set_e))
set_d.symmetric_difference_update(set_e)
print("after")
print(set_d)
print(set_e)

print("check subset in another set")
set_d = {1,2,3,4}
set_e = {5,6,7,8}
print(set_d)
print(set_e)
print(set_d.isdisjoint(set_e)) #True
set_d = {1,2,3,4}
set_e = {1,2,3,4,5,6,7,8}
print(set_d)
print(set_e)
print(set_d.isdisjoint(set_e)) #False
print(set_d.issubset(set_e)) #True
print(set_d.issuperset(set_e)) #False
print(set_e.issuperset(set_d)) #True
