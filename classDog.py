class Dog :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def bark(self) :
        print(self.name, 'is barking')

x = Dog('Jack', 3)
y = Dog('Daisy', 2)

x.bark()
y.bark()

print(x.name, 'is', x.age, 'years old.')
print(y.name, 'is', y.age, 'years old.')
