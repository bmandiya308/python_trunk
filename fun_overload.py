def func_call(a,b):
    print("Two paramer")
func_call(10,20)
def func_call(a,b,c):
    print("three paramer")
func_call(10,20,30)


# Function to take multiple arguments
def add(datatype, *args):
    if datatype =='int':
        answer = 0
    if datatype =='str':
        answer =''
    for x in args:
        answer = answer + x
    print(answer)

add('int', 5, 6)
add('str', 'Hi ', 'Geeks')
