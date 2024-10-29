class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('%s is running...' % self.name)


person = Person('John', 23)
person.run()
