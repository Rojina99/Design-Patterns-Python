class Singeleton(object):
    instance = None

    #classmethod
    def Instance(cls):
        if cls.instance == None:
            cls.instance = Singeleton()
        return cls.instance

    def __init__(self):
        if self.instance!= None:
            raise ValueError("A singeleton instance is already existing")

    def SetData(self, num):
        self.data = num

    def GetData(self):
        return self.data

obj = Singeleton()
obj.Instance().SetData(num="5")
print(obj.Instance().GetData())

obj = Singeleton()
Singeleton.Instance(obj).SetData("10")
print(obj.Instance().GetData())

a = Singeleton().Instance()
a.SetData("100")
print(a.GetData())