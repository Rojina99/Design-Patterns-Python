class Component:
    def Operation(self):
        raise NotImplementedError("Operation() must be defined in subclass")

class ConcreteComponent(Component):
    def Operation(self):
        print("Inside ConcreteComponent: Operation()")

class Decorator(Component):
    def __init__(self, obj):
        self.comp = obj

    def Operation(self):
        print("Inside Decorator: Operation()")
        self.comp.Operation()

class ConcreteDecoratorA(Decorator):
   def __init__(self, obj):
       Decorator.__init__(self, obj)
       self.addedState = None

   def Operation(self):
       Decorator.Operation(self)
       self.addedState = 1
       print("ConcreteDecoratorA : Operation()")
       print("ConcreteDecoratorA : addedState= ", self.addedState)

class ConcreteDecoratorB(Decorator):
    def __init__(self, obj):
        Decorator.__init__(self, obj)
        self.addedState = None

    def Operation(self):
        Decorator.Operation(self)
        self.addedState = 1
        print("ConcreteDecoratorB : Operation()")
        print("ConcreteDecoratorB : addedState= ", self.addedState)

myComponent = ConcreteDecoratorA(ConcreteDecoratorB(ConcreteComponent()))
myComponent.Operation()