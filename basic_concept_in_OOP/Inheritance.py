class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

my_dog = Dog("Buddy")
print(my_dog.speak()) 

my_cat = Cat("Whiskers")
print(my_cat.speak())  
