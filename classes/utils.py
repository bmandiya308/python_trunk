class Parent_1:
    def __init__(self):
        print("Parent_1")
    def package_name(self):
        return __package__
    def parent_2_def(self):
        #print("parent_1_def")
        return "parent_1_def"

class Parent_2:
    def __init__(self):
        print("Parent_2")
    def package_name(self):
        return __package__
    def parent_2_def(self):
        #print("parent_2_def")
        return "parent_2_def"
    def extra_def(self):
        return "extra_def 1 2 3"

class Child(Parent_1,Parent_2):
    def __init__(self):
        self._name = 'Bhaskar'
        self.__sirname = 'Mandiya'
        #Parent_2.__init__(self)
        #super(Child, self).parent_2_def()
    def two_par(self,a,b):
        return a + b
    def two_par(self,a,b,c):
        return a + b + c

a = Child()
print(a.package_name)
print(a.parent_2_def())
print(a.extra_def())
#print(a.two_par(1,2))  ##will give error
print(a.two_par(1,2,3))
print(a._name)
#print(Child._name) it will not work
print(a._Child__sirname)
print(Child.__mro__)
