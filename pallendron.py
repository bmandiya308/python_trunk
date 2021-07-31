def reversed(s):
    rev = s[::-1]
    return rev

input_str = str(input("Please enter string to check pallendrom"))
rev = reversed(input_str)
if(rev == input_str):
    print("pallendrom")
else:
    print("Not a pallendromj")
