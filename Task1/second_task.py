class Car:
    def __init__(self,motor,wheel=4):
        self.wheel = wheel
        self.motor = motor
        print("number of wheel is",self.wheel, "and the motor is",self.motor) 
first_car = Car("motor1")
second_car = Car("motor2",10)
print(type(first_car))
print(type(second_car))
        