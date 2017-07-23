class Context:
    def __init__(self):
        self.strategy = None

    def SetStrategy(self, obj):
        self.strategy = obj

    def GetStrategy(self):
        return self.strategy

    def ContextInterface(self):
        self.strategy.AlgorithmInterface()

class Strategy():
    def AlgorithmInterface(self):
        raise NotImplementedError("AlgorithmInterface must be implememted in subclass")

class ConcreteStrategyA(Strategy):
    def AlgorithmInterface(self):
        print("Inside ConcreteStrategyA: AlgorithmInterface()")

class ConcreteStrategyB(Strategy):
    def AlgorithmInterface(self):
        print("Inside ConcreteStrategyB: AlgorithmInterface()")

class ConcreteStrategyC(Strategy):
    def AlgorithmInterface(self):
        print("Inside ConcreteStrategyC: AlgorithmInterface()")


context = Context()

conStrategyA = ConcreteStrategyA()
context.SetStrategy(conStrategyA)
context.ContextInterface()

context.SetStrategy(ConcreteStrategyB())
# context.GetStrategy()
context.ContextInterface()

context.SetStrategy(ConcreteStrategyC())
context.ContextInterface()

