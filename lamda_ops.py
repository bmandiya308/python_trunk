# Python code to illustrate cube of a number  
# showing difference between def() and lambda(). 
def cube(y): 
    return y*y*y; 
  
c = lambda x: x*x*x
s = lambda x: x*x
print(c(5))
print(s(5))
print(cube(5))

print("Use that function definition to make a function that always doubles the number you send in:")
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print("Doubling 11,12,15 Numbers as below :")
print(mydoubler(11))
print(mydoubler(12))
print(mydoubler(15))

# Python code to illustrate
print("filter() with lambda()")

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

print("try to modify in filter to get square of odd")
final_list_mod_odd = list(map(lambda x:x * x ,filter(lambda x: (x%2 != 0), li)))
print("try to modify in filter to get square of even")
final_list_mod_even = list(map(lambda x: x * x ,filter(lambda x: (x%2 == 0), li)))

print("Original :\n",li)
print("Modified Odd:\n",final_list_mod_odd)
print("Modified Even:\n",final_list_mod_even)

print("Filter with def function")

def check_even(item):
    if(item % 2 == 0):
        return True
    return False

final_list_1 = filter(check_even, li)
for elem in final_list_1:
    print("Even Number : ",elem)

# Python code to illustrate
print("map() with lambda()")
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)

# Python code to illustrate
print("reduce() with lambda()")
# to get sum of a list
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print("Original :\n",li)
print ("Sum of Items :\n",sum)
sum_1 = reduce(lambda x, y: x + y, li)
print ("Sum of Items_1 :\n",sum_1)

#dict_a = reduce(lambda x, y: {x : y}, li)
#print(dict_a)
print("Get max Element from below list :")
list_max = [1,2,8,3,5,9,6,4,100,34,23,24,5,7]
print("Original :\n",list_max)
print("Max Element :")
print (reduce(lambda a,b : a if a > b else b,list_max))
print (reduce(lambda a,b : a if a < b else b,list_max))
