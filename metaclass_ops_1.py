DataCampClass = type('DataCamp', (), {})
print(DataCampClass)
print(DataCampClass())

PythonClass = type('PythonClass', (), {'start_date': 'August 2018', 'instructor': 'John Doe'} )
print(PythonClass.start_date, PythonClass.instructor)
print(PythonClass)

article = 'metaclasses'
print(article)
print(article.__class__)
print(article.__class__.__class__)
print(type(article))
print(type(list),type(float), type(dict), type(tuple))


print("-------Custom MetaClass--------")

class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubclass(MyClass):
    pass

print(type(MyMeta))
print(type(MyClass))
print(type(MySubclass))
'''
OUTPUT :
<class 'type'>
<class '__main__.MyMeta'>
<class '__main__.MyMeta'>
'''

print("Sigleton class : ")

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self,num):
        self.num=num
    def get_number(self):
        return self.num

a = SingletonClass(10)
b = SingletonClass(20)

print(a.get_number())
print(b.get_number())
