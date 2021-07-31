list_1 = list(range(1,11))
list_2 = list(range(11,21))

final_dic = {x:y for x,y in zip(list_1,list_2)}

# for key in final_dic.keys():
#     print(key," - ",final_dic[key])



#print(final_dic)


#
#
# final_dic[2] = 38
# final_dic[5] = 31
#
# #
# # for key,valaue in sorted(final_dic.items(),key=lambda kv: kv[1]):
# #     print(key," - ",valaue)
#
# sorted_by_value = {x:y for x,y in sorted(final_dic.items(),key=lambda x : x[1])}
# print("Sorted by Values")
#
# for i in sorted_by_value.keys():
#     print(i," - ",final_dic[i])
#
# sorted_by_keys = {x:y for x,y in sorted(sorted_by_value.items())}
#
# print("Sorted by keys")
#
# for i in sorted_by_keys.keys():
#     print(i," - ", sorted_by_keys[i])
#
# import pickle
# class ABC:
#     def __init__(self):
#         self.a = 100
#
# abc_obj = ABC()
# str = pickle.dumps(abc_obj)
# print(str)
# a1 = pickle.loads(str)
# #print(a1.a)
#
# import copy
#
# a2 = copy.copy(a1)
# print(a1.a)
# print(a2.a)
# a2.a = 200
# print("after change : COPY")
# print(a1.a)
# print(a2.a)
#
# a3 = copy.deepcopy(a2)
# print("before")
# print(a2.a)
# print(a3.a)
#
# print("AFTER : ")
# a3.a = 300
# print(a2.a)
# print(a3.a)
#



for i in range(1,11):
    print(type(type(i)))
    print(type(int))

int_a = int(input("Gte the Number : "))
print(int_a)