list_a = list(range(1,12))
list_c = list(range(10,21))

print("type and reverse")
print(type(list_a))
#reverse
print(list(reversed(list_a)))
#reverse type <class 'list_reverseiterator'>
print(type((reversed(list_a))))
list_c.reverse()
print(list_c)

print("Add")
list_a.append(11)
print(list_a)
list_a.insert(1,100)
print(list_a)

print("remove")
list_a.remove(100)
print(list_a)
list_a.pop(4) #indexing delete
print(list_a)
list_b = list_a.copy()
del list_a[0]
del list_a[0:3]
del list_a[9:]
print(list_a)
list_a.clear()
print(list_a)
print(list_b)

print("count")
list_b.append(10)
count_num = list_b.count(10)
print(count_num)
print(len(list_b))

print("sort list items")
list_b.sort()
print(list_b)

print("append another list")
list_b.extend(list_c)
list_b.sort()
print(list_b)

print("index")
print(list_b.index(10))

print("find dublicate items in list")
set_a = list()
for item in list_b:
    if(list_b.count(item) >= 2):
        set_a.append(item)
print(set(set_a))

print("formatting values")
formatted_list = [x for x in list_b if x % 2 == 0]
print(formatted_list)

print("Checking item available")
if 20 in formatted_list:
    print("its there",20)
if 21 not in formatted_list:
    print("its not there",20)
