




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        print('Person name is: ',self.name)
person1 = Person('Python',34)

person1.display_name()
