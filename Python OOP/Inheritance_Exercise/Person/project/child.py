from Person.project.person import Person
# from project.person import Person For Judge

class Child(Person):

    def __init__(self, name, age):
        Person.__init__(self, name,age)



person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)