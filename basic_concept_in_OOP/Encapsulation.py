class Car:
    def __init__(self, make, model, year):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self.__year = year  # private attribute

    def get_info(self):
        return f"{self.__make} {self.__model}, {self.__year}"

    def set_year(self, year):
        if year > 1885:  # the first car was made in 1886
            self.__year = year
        else:
            print("Invalid year!")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_info())  
my_car.set_year(2022)
print(my_car.get_info())  
