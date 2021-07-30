dict_a = {1:'a',2:'b',3:'c',4:{4:'d',5:'doctor'},5:'e'}
print(dict_a)
print("add item in dictionary")
dict_a[5] = {5:'e',6:'elephant'}
print(dict_a)

print("delete dictionaly")
del dict_a[5][5]
dict_b = dict_a.copy()
dict_b[100] = 'B'
print(dict_a)
print(dict_b)
dict_a.pop(2) #delete where key = 2
dict_a.popitem() #delete last ietm
print(dict_a)
print(dict_a)
dict_a.clear()
print(dict_a)

print("Get elements")
dict_b[8] = 'Bhaskar'
dict_b[7] = 'Mandiya'
print(dict_b.get(5)) #get value. Will not raise nay error if not present
print(dict_b.items())
print(dict_b.keys())
print(dict_b.values())

'''
print("iterating by items")
for key,value in sorted(dict_b.items()):
    print(key," - ",value)


print("iterating by keys")
for key in sorted(dict_b.keys()):
    print(key," - ",dict_b[key])

# failenwhen elements are diff type
dict_c = {1:'Mandiya',2:'Bhaskar',3:'Khangaon'}
print("iterating by keys")
for value in sorted(dict_c.values()):
    print(value," - ",value)
'''

dict_c = {1:'Mandiya',2:'Bhaskar',3:'Khangaon'}
print("update dictionary")
dict_c.update({10:'Maharashtra'})
dict_c.update({100:{10 : 'Savings'}})
print(dict_c[100][10])  ##Saving
print(dict_c)
print(dict_c.fromkeys(dict_c.keys(),dict_c.values())) #take keys from list and create dictionary if value not provided the None

print("substitution")
print(dict_c)
x = dict_c.setdefault(2,'BhaskarRao')
y = dict_c.setdefault(5,'If None the put')
print(dict_c)
print(x)
print(y)

