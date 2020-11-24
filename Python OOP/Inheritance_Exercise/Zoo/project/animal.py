class Animal:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


# an = Animal("daniel")
# print(an.name)