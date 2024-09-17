# inheritance

class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    def driving(self):
        print("Car is used for driving")

# Audi car is inherting from Car class
class Audi(Car):
    def __init__(self,windows,doors,enginetype,horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower=horsepower

    def selfdriving(self):
        print("Audi is a self driving car")


audi_new = Audi(4,5,"Diesel",200)

print(audi_new.horsepower)
print(audi_new.windows)
audi_new.driving()
audi_new.selfdriving()

print("__________________")

car1=Car(4,5,"Diesel")
print(car1)
print(audi_new)

print(dir(audi_new))
print(dir(car1))



