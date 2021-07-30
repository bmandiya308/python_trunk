def lch(list1,list2,indx):
    if(indx >= 0):
        print(list1[indx],list2[indx])
        return lch(list1,list2,indx-1)
    else:
        exit(1)
list1 = list(range(0,11))

list2 = [i * -1 for i in range(0,11)]

print(lch(list1,list2,len(list1)-1))