class ABC():
    def __init__(self,max):
        self.max = max

    def __iter__(self):
        self.id = 0
        return self
    def __next__(self):
        self.id = self.id + 1
        if(self.id <= self.max):
            return self.id
        else:
            raise StopIteration


a = ABC(5)
i = iter(a)
print(type(a))
print(type(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))