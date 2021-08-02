import time
def get_decorator(fun):
    print("Decorator")
    def inner():
        print("Its an inner fun")
        print(time.time())
        fun()
        print(time.time())
    return inner

@get_decorator
def func_to_get_decorate():
    print("Its a normal function")

func_to_get_decorate()
