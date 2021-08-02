def func_simple(a):
    print(a)
def fun_var(a,b):
    print(a," - ",b)
def func_list(*arr):
    print(arr[4])
def func_dict(**arr):
    print(arr['c'])

func_simple(10)
fun_var(b=10,a=20)
func_list(1,2,3,4,5,6,7,8,9)  ##*args
func_dict(a=12,b=45,c=63,d=747)  ##**kwargs
