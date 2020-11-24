# from Zoo.project.animal import Animal
from project.animal import Animal


class Reptile(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

