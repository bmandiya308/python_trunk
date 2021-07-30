num = int(input("Please enter number : "))
check = 1
while(num > 0):
    a = 0
    for i in (range(2,check+1)):
        if(check % i == 0):
            a +=1
    if(a <= 1):
        print("Prime number : ",check)
    else:
        print("not a prime number : ",check)
    num -= 1
    check += 1
