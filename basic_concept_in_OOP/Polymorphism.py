class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} is flying"

class Penguin(Bird):
    def fly(self):
        return f"{self.name} can't fly but can swim"

def make_it_fly(bird):
    print(bird.fly())

sparrow = Bird("Sparrow")
penguin = Penguin("Penguin")

make_it_fly(sparrow)  
make_it_fly(penguin)  
