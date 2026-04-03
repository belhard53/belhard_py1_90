from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str = 'SomeName'):
        self.name = name


    @abstractmethod
    def says(self):
        pass


class Cat(Animal):
    def says(self):
        return f"{self.name} - кошка. Говорит МЯУ!"


class Dog(Animal):
    def says(self):
        return f"{self.name} - собака. Говорит ГАВ!"


class Cow(Animal):
    def says(self):
        return f"{self.name} - корова. Говорит МУ-МУ!"


# murzik = Cat("Мурзик")
# mumu = Dog("Муму")
# musya = Cow("Муся")


# print(murzik.says())
# print(mumu.says())
# print(musya.says())
