num = int(input("Enter number"))
temp = num
while(num > 0):
    num1 = num
    temp_1=num
    star_str = ""
    while(num1 > 0):
        star_str = star_str + " * "
        num1 -= 1
    while(temp_1 < temp):
        star_str = " "+star_str
        temp_1 += 1
    print(star_str)
    num -= 1
bk =temp
while(temp > 0):
    num1 = temp
    temp_1=1
    star_str = ""
    while(num1 <= bk):
        star_str = star_str + " * "
        num1 += 1
    while(temp_1 < temp):
        star_str = " "+star_str
        temp_1 += 1
    print(star_str)
    temp -= 1

