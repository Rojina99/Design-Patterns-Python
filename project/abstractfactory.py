class AbstractFactory:
    def CreateProduct1(self):
        raise NotImplementedError("Create Product1() must be defined in sub class")
    def CreateProduct2(self):
        raise NotImplementedError("Create Product2() must be defined in sub class")

class ConcreteFactory1(AbstractFactory):
    def CreateProduct1(self):
        return Product1_1()
    def CreateProduct2(self):
        return Product2_1()

class ConcreteFactory2(AbstractFactory):
    def CreateProduct1(self):
        return Product1_2()
    def CreateProduct2(self):
        return Product2_2()

class AbstractProduct1:
    def Display(self):
        raise NotImplementedError("Display() must be defined in subclass")

class Product1_1(AbstractProduct1):
    def Display(self):
        print("Inside Product1_1: Display()")

class Product1_2(AbstractProduct1):
    def Display(self):
        print("Inside Product 1_2: Display()")

class AbstractProduct2:
    def Display(self):
        raise NotImplementedError("Display() must be defined in subclass")

class Product2_1(AbstractProduct2):
    def Display(self):
        print("Inside Product 2_1: Display()")

class Product2_2(AbstractProduct2):
    def Display(self):
        print("Inside Product 2_1: Display()")

# Series one Products
factory1 = ConcreteFactory1()
prod1 = factory1.CreateProduct1()
prod1.Display()
prod2 = factory1.CreateProduct2()
prod2.Display()

#Series two products
factory2 = ConcreteFactory2()
prod1 = factory2.CreateProduct1()
prod1.Display()
prod2 = factory2.CreateProduct2()
prod2.Display()