def add(*args):
    for numbers in args:
        return sum(args)

print( add(7,9,50))


def calculate (n,**kwargs):
    print(type(kwargs))
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)
calculate(2,add=2,multiply = 5)

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make="Alfa", model="GT")
print(my_car.make)