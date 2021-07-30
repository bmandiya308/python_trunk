class Parent:
    def __init__(self,fname,lname,city):
        self.fname = fname
        self.lname = lname
        self.city = city

    def get_all(self):
        return self.fname + " : " + self.lname + " : " + self.city
    def parent_def(self):
        print("Its a Parent def")

class Child(Parent):
    def __init__(self,fname,lname,city):
        Parent.__init__(self,fname,lname,city)

    def child_def(self):
        print("its a child def")

c_obj = Child('Bhaskar','Mandiya','Khangaon')
print(c_obj.get_all())
c_obj.parent_def()
c_obj.child_def()


class Parent1:
    def __init__(self,fname,lname,city):
        self.fname = fname
        self.lname = lname
        self.city = city

    def get_all(self):
        return self.fname + " : " + self.lname + " : " + self.city
    def parent_def(self):
        print("Its a Parent def")

class Child1(Parent):
    def __init__(self,fname,lname,city):
        self.fname = fname
        self.lname = lname
        self.city =city

print("Second scena")
ch1_obj = Child1('Ketan','Kubde','Wani')
print(c_obj.get_all())
ch1_obj.parent_def()
par_obj = Parent('Sachin','Bairagi','Bildhana')
par_obj.parent_def()
