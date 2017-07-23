class Director:
    def __init__(self):
        self.builder = None

    def SetBuilder(self, builderObj):
        self.builder = builderObj

    def Contract(self, name):
        if name=="Product1":
            self.builder.Create()
            self.builder.BuildPartA()
            self.builder.BuildPartB()
        elif name=="Product2":
            self.builder.Create()
            self.builder.BuildPartC()
            self.builder.BuildPartD()

class Builder:
    def Create(self):
        raise NotImplementedError("Create() must be defined in subclass")

    def BuildPartA(self):
        raise NotImplementedError("BuildPartA() must be defined in subclass")

    def BuildPartB(self):
        raise NotImplementedError("BuildPartB() must be defined in subclass")

    def BuildPartC(self):
        raise NotImplementedError("BuildPartC() must be defined in subclass")

    def BuildPartD(self):
        raise NotImplementedError("BuildPartD() must be defined in subclass")

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = None

    def Create(self):
        self.product = Product1()

    def BuildPartA(self):
        pass

    def BuildPartB(self):
        pass

    def BuildPartC(self):
        pass

    def BuildPartD(self):
        pass

    def GetProduct(self):
        return self.product

class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = None

    def Create(self):
        self.product = Product2()

    def BuildPartA(self):
        pass

    def BuildPartB(self):
        pass

    def BuildPartC(self):
        pass

    def BuildPartD(self):
        pass

    def GetProduct(self):
        return self.product

class Product1:
    def UseProduct(self):
        print("Inside Product1: UseProduct()")

class Product2:
    def UseProduct(self):
        print("Inside Product2: UseProduct()")


director = Director()

builder1 = ConcreteBuilder1()
director.SetBuilder(builder1)
director.Contract("Product1")
builder1.GetProduct().UseProduct()

builder2 = ConcreteBuilder2()
director.SetBuilder(builder2)
director.Contract("Product2")
builder2.GetProduct().UseProduct()

