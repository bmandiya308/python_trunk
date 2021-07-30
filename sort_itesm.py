list_a = [1,'Bhaskar','Mandiya',23,'Khangaon']
print(list_a)
list_a = [str(i) for i in list_a]
for i in sorted(list_a):
    print(i)

tuple_a = (1,'Bhaskar','Mandiya',23,'Khangaon')
print(type(tuple_a))
print(tuple_a)
tuple_a = (str(i) for i in tuple_a)
print(type(tuple_a))
for i in sorted(tuple_a):
    print(i)

list_a = {1,'Bhaskar','Mandiya',23,'Khangaon'}
print(type(list_a))
print(list_a)
list_a = set([str(i) for i in list_a])
for i in sorted(list_a):
    print(i)

print("Dictionary valuation ")
dict_a = {'5':'Sakharam','1':1000,'2':'Ketan','b':'Babulal','a':'Sachin'}
for i in sorted(dict_a.keys()):
    print(i," ",dict_a[i])

for i,b in sorted(dict_a.items()):
    print(i," ",b)

for i in sorted(dict_a.keys()):
    print()
    dict_a[i] = str(dict_a[i])

print(dict_a)

for i in sorted(dict_a.values()):
    print(i)
