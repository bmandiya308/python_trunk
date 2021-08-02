from typing import Any, Union

input_num = int(input("Please enter number to check palendrom"))
mul = 0
temp = input_num
while(input_num > 0):
    dig = int (input_num % 10)
    mul = mul * 10 + dig
    input_num = input_num // 10

print(mul)
print(temp)
