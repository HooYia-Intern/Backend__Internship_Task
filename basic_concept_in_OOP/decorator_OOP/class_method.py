class Car:
    def __init__(self, wheel):
        self.wheel = wheel
        self.name = "class car"

    @classmethod
    def get_info(cls):
        return dir(cls)

# Example usage:
my_car = Car(4)
print(my_car.wheel)  # Output: 4
print(my_car.name)   # Output: class car
print(Car.get_info())  # Output: List of attributes and methods of the Car class
