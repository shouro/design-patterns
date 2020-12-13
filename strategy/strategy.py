import abc


class InterfaceFly(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        raise NotImplementedError


class InterfaceQuack(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        raise NotImplementedError


class InterfaceDisplay(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def display(self):
        raise NotImplementedError

class SimpleFly(InterfaceFly):
    def fly(self):
        print('simple fly')

class SimpleQuack(InterfaceQuack):
    def quack(self):
        print('simple quack')

class SimpleDisply(InterfaceDisplay):
    def display(self):
        print('simple display')

class WildFly(InterfaceFly):
    def fly(self):
        print('wild fly')

class WildQuack(InterfaceQuack):
    def quack(self):
        print('wild quack')

class WildDisply(InterfaceDisplay):
    def display(self):
        print('wild display')

class Duck():
    def __init__(self, fly_strategy, quack_strategy, display_strategy):
        self.fly_strategy = fly_strategy
        self.quack_strategy = quack_strategy
        self.display_strategy = display_strategy
    
    def fly(self):
        self.fly_strategy.fly()
    
    def quack(self):
        self.quack_strategy.quack()
    
    def display(self):
        self.display_strategy.display()
    
    def demo(self):
        self.fly()
        self.quack()
        self.display()


if __name__ == "__main__":
    sf = SimpleFly()
    sq = SimpleQuack()
    sd = SimpleDisply()
    simple_duck = Duck(sf, sq, sd)
    simple_duck.demo()

    wf = WildFly()
    wq = WildQuack()
    wd = WildDisply()
    wild_duck = Duck(wf, wq, wd)
    wild_duck.demo()
