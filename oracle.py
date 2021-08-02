

list_input = ["may", "student", "students", "dog","studentssess", "god","god","cat", "act","tab", "bat", "flow", "wolf", "lambs","amy", "yam", "balms", "looped", "poodle"]

'''
list_matched =list()
list_not_matched =list()
for word in list_input:
    length_match = [itm for itm in list_input if len(word) == len(itm) and word != itm]
    #print(length_match)
    if(len(length_match) <= 0):
        next
    else:
        for word1 in length_match:
            count = 0
            for char in word:
                if(char in word1):
                    count += 1
            if(len(word1) == count):
                if(not word in list_matched):
                    list_matched.append(word)

print(list_matched)
print(list_not_matched)


dict_a = dict()

for word in list_input:
    if(not dict_a.get(word)):
        dict_a[word] = {'value' : ''.join(sorted(list(word))), 'count' : 1}
    else:
        dict_a[word] = {'value': ''.join(sorted(list(word))), 'count': dict_a[word]['count'] + 1}

print(dict_a)

for key,value in sorted(dict_a.items(),key=lambda x:x[1]):
    dict_bk = dict_a.copy()
    del dict_bk[key]
    if(value in dict_bk.values()):
        print("Matched : ",key)
    else:
        print("Not Matched : ",key)

'''


dict_a = dict()

for word in list_input:
    if(not dict_a.get(''.join(sorted(list(word))))):
        dict_a[''.join(sorted(list(word)))] = [word]
    else:
        dict_a[''.join(sorted(list(word)))].append(word)

for key,value in dict_a.items():
    print(key,' : ',value)




