import abc
import random
import pprint
import time


class IObserver(metaclass=abc.ABCMeta):
    abc.abstractmethod
    def update(self):
        raise NotImplementedError


class IObservable(metaclass=abc.ABCMeta):
    abc.abstractmethod
    def add(self, IObserver):
        raise NotImplementedError
    
    abc.abstractmethod
    def remove(self, IObserver):
        raise NotImplementedError

    abc.abstractmethod
    def notify(self):
        raise NotImplementedError


class weatherStation(IObservable):
    def __init__(self):
        self.state = {}
        self.observer_list = []

    def add(self, IObserver):
        self.observer_list.append(IObserver)
    
    def remove(self, IObserver):
        try:
            self.observer_list.remove(IObserver)
        except ValueError as ve:
            print(ve)
            print('failed to remove observer')
    
    def notify(self):
        self._setState()
        for observer in self.observer_list:
            observer.update()

    def getState(self):
        return self.state
    
    def _setState(self):
        temperature = [i for i in range(0, 101)]
        humidity = [i for i in range(0, 101)]
        presure = [i for i in range(1, 101)]
        self.state = {
            'temperature': random.choice(temperature),
            'humidity': random.choice(humidity),
            'presure': random.choice(presure),
        }


class weatherClient(IObserver):
    def __init__(self, observable):
        self.data = {}
        self.observable = observable
    
    def update(self):
        self.data = self.observable.getState()

    def show(self):
        print(self.data)


def simulate():
    station = weatherStation()
    client_1 = weatherClient(station)
    client_2 = weatherClient(station)
    station.add(client_1)
    station.add(client_2)
    tick = 5
    while(tick > 0 ):
        station.notify()
        client_1.show()
        client_2.show()
        time.sleep(2)
        tick = tick - 1

if __name__ == "__main__":
    simulate()
