# list_a = [1,2,3,4,5,6,7]
# list_b = [-1,-2,-3,-4,-5,-6,-7]
# list_f = list()
# # for item1 in list_a:
# #     list_f.append(item1)
# #     for item in list_b:
# #         list_f.append(item)
# #         list_b.remove(item)
# #         break
#
#
#
#
# list_d = list(zip(list_a,list_b))
# # print(list_d)
# #
# list_e = list()
#
# for i in list_d:
#     for indx in range(len(i)):
#         list_e.append(i[indx])
# print(list_e)
#
# from functools import reduce
# import operator
#
# # a = reduce(operator.add,zip(list_a,list_b))
# # print("end")
# # print(a)
# # print("end")
# #
# # # Driver code
# # lst1 = [1, 2, 3]
# # lst2 = ['a', 'b', 'c']
# # print("Reduce")
# # #print(list(countList(lst1, lst2)))
# # print("Reduce")
# import functools
# # print(functools.reduce(operator.add,zip(list_a,list_b)))
# for i in list(functools.reduce(lambda x,y: x+y,zip(list_a,list_b))):
#    print(i)
#
# import functools
# print("start")
# for i in list(functools.reduce(lambda x,y: x+y,zip([1,2,3],[4,5,6]))):
#     print(i)
#
# #print(functools.reduce(lambda x,y: x+y,[1,2,3,4]))
#
# tup1 = (1,2)
# tup2 = (3,4)
# print(list(tup1 + tup2))
#
#
#
# list_a = [1,2,3,4,5,6,6,7,8,8,98,9,9,90,9,0,6.7,8,9]
#
# event_list = list(filter(lambda x: x if x%2!=0 else None,list_a))
# print(event_list)
#
# print("filter")
# list_e = list(filter(lambda x: (x%2==0),range(0,10)))
# print(list_e)
# print("map")
# list_e = list(map(lambda x: (x%2==0),range(0,10)))
# print(list_e)
# list_e = list(map(lambda x: x if x%2==0 else None,range(0,10)))
# print(list_e)
# list_e = list(filter(lambda x: (x is not None) ,list(map(lambda x: x if x%2==0 else None,range(0,10)))))
# print(list_e)
# print("reduce")
# list_e = reduce(lambda x,y: x+y,range(0,11))
# print(list_e)
#
# list_e = reduce(lambda x,y:x+y,zip([1,2,3,45],[4,5,6,46]))
# print(list_e)

#
# import os


# num = int(input("Enter number for palydrom : "))
# temp = num
# mul = 0
#
# while(num > 0):
#     dig = num % 10
#     mul = mul * 10 + dig
#     num = num // 10
#     print("dig : ",dig," mul : ",mul," num: ",num)
#
# print(mul)
# i=0
# limit = int(input("Enter Limit buddy : "))
# while(i < limit):
#     pr_str = ""
#     j = limit
#     while(j >= i):
#         #print(i,j)
#         pr_str = pr_str + " "
#         j -= 1
#     k = i
#     while(k > 0):
#         pr_str = pr_str + " *"
#         k -= 1
#     print(pr_str)
#     i+=1
#
#
# i=0
# while(i < limit ):
#     pr_str = ""
#     j = i
#     while(j >= 0):
#         #print(i,j)
#         pr_str = pr_str + " "
#         j -= 1
#     k = i
#     while(k <= limit - 1):
#         pr_str = pr_str + " *"
#         k += 1
#     print(pr_str)
#     i+=1

#
list1 = [1,2,3,4,5,6,7,8]
list2 = [-1,-2,-3,-4,-5,-6,-7,-8]
# import operator
# import functools
#
# print(functools.reduce(operator.add,zip(list1,list2)))

# print([sub[indx] for indx in range(len(list1)) for sub in [list1,list2]])

list3 = list()
#
# for i in list1:
#     list3.append(i)
#     for j in list2:
#         list3.append(j)
#         list2.remove(j)
#         break
#
# print(list3)


j=0


# for j in range(len(list1)):
#     for i in [list1, list2]:
#         list3.append(i[j])
#
# print(list3)


# Return double of n
# def addition(n):
#     return n + n


# We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))


# list3 = [1,4,65,3,23,67,99,34,98,44,102,113,88]
#
# print(list(filter(lambda x : x % 2 == 0,list3)))
# import functools
# print(functools.reduce(lambda x,y : x if x > y else y,filter(lambda x : x % 2 == 0,list3)))
#
#
# for i in sorted(list3):
#     print(i)

# dict_1 = {1:34,4:56,2:12,5:67}
#
# for i,j in sorted(dict_1.items(),key=lambda x : x[1],reverse=True):
#     print(i,j)


# class ABC:
#     def __init__(self,name):
#         self.a = 10
#         self.name = name
#     def get_name(self):
#         return self.name
#
# import pickle
# a = ABC("Bhaskar")
# print(a.name)
# print(a.a)
# obj_str = pickle.dumps(a)
# #print(obj_str)
# out = open('obj.txt','wb')
#
# pickle.dump(a,out)
# out.close()
#
# out = open('obj.txt','rb')
# b = pickle.load(out)
#
# #
# print(b.a)
# print(b.name)
#

'''

str1  = "Bhaskar"

list1 = list(str1)

for i in str1:
    print(i)

'''

##iterartor__iter__
'''
import time
def decorator_func(func):
    def decorates():
        print("decorates started")
        print(time.time())
        func()
        print(time.time())
        print("decorates END")
    return decorates

@decorator_func
def abc():
    print("this is my main function")


abc()




list1 = [34,23,3,67,12,34,22,32,98,56,31,9]

a = {
    'five' : 5,
    'ten'  : 10,
    'one'  : 1,
    'four' : 4
    }

for i in sorted(a.items(),key=lambda x : x[1]):
    print(i)
'''


# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return (dict2.update(dict1))


# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This return None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict1)
print(dict2)

