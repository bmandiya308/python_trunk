class SingletonGovt:
    __instance__ = None
    @staticmethod
    def getinstance(id):
        if SingletonGovt.__instance__ is None:
            SingletonGovt(id)
        return SingletonGovt.__instance__

    def __init__(self,id):
        """ Constructor.
        """
        if SingletonGovt.__instance__ is None:
            self.id = id
            SingletonGovt.__instance__ = self
        else:
            raise Exception("This class is a singleton!")



a = SingletonGovt(10)
#b = SingletonGovt(20)
print(a.id)
b = SingletonGovt.getinstance(20)
print(b.id)

