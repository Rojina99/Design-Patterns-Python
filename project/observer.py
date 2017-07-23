class Subject:
    observers = []

    def Attach(self, obj):
        self.observers.append(obj)

    def Detach(self, obj):
        pass

    def Notify(self):
        for observer in self.observers:
            observer.Update()
        # print(self.observers)
class ConcreteSubject(Subject):
    def __init__(self):
        self.state = None

    def SetState(self, value):
        self.state = value
        self.Notify()

    def GetState(self):
        return self.state

class Observer:
    def Update(self):
        raise NotImplementedError("Update() must be defined in subclass")

class ConcreteObserverA(Observer):
    def __init__(self, obj):
        self.conSub = obj
        self.conSub.Attach(self)

    def Update(self):
        print("Inside ConcreteObserverA: Update()")
        self.state = self.conSub.GetState()
        print("State ", self.state)

class ConcreteObserverB(Observer):
    def __init__(self, obj):
        self.conSub = obj
        self.conSub.Attach(self)

    def Update(self):
        print("Inside ConcreteObserverB: Update()")
        self.state = self.conSub.GetState()
        print("State ", self.state)

conSubObj = ConcreteSubject()
obsObj1 = ConcreteObserverA(conSubObj)
obsObj2 = ConcreteObserverB(conSubObj)
conSubObj.SetState(1)
conSubObj.SetState(2)
# obsObj1.Update()
# obsObj2.Update()