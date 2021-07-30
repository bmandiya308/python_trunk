class A(object):
    def __new__(cls, *args, **kwargs):
        print("New")
        return
    def __call__(self, *args, **kwargs):
        print("Call")
        return

class E(metaclass=A):
    def __init__(self):
        print(__class__)
# class F(E):
#     def __init__(self):
#         print(__class__)

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    def __init__(self):
        print("its ",__class__)

#F()
print("Class A")
print(isinstance(A,type))
print(isinstance(A,object))
print(issubclass(A,type))
print(issubclass(A,object))

print("Class B")
print(isinstance(B,type))
print(isinstance(B,object))

print("Class C")
print(isinstance(C,type))
print(isinstance(C,object))

print("Class D")
print(type(D))
print(isinstance(D,type))
print(isinstance(D,object))

print("Class E")
print(type(E))
print(isinstance(E,object))
print(isinstance(E,type))
print(type(E))
print(type(type))
print(type(object))

print("-----------------Class------------------------")

print(issubclass(type,object))
print(issubclass(object,object))
print(issubclass(object,type))
print(issubclass(type,type))
print(issubclass(A,A))
print(issubclass(B,A))

print("-----------------Class------------------------")

print(isinstance(type,object))
print(isinstance(object,object))
print(isinstance(object,type))

#print(issubclass(E,object))
#print(issubclass(E,type))

