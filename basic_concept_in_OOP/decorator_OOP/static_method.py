class Car:
    def __init__(self, wheel):
        self.wheel = wheel
        self.name = "class car"

    @staticmethod
    def get_class_info():
        return "This is the child class"

# Example usage:
my_car = Car(4)
print(my_car.wheel)  # Output: 4
print(my_car.name)   # Output: class car
print(Car.get_class_info())  # Output: This is the child class
