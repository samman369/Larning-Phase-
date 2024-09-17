# classes --> Real world Entity or object
# attributes --> properties of the class
# methods --> actions of the class

class Car:
    pass

# cretae object of class
car1= Car()
car2= Car()

car1.glass=4
car1.seat=4
car1.engine="diesel"

car2.glass=6
car2.seat=6
car2.engine="petrol"

# print engine type
print(car1.engine)
print(car2.engine)

# it will show the defult in built method
print(dir(car1))


# Let's have a good look of class
class Car:
    # constructor
    def __init__(self,windows,tyres,engine):
        self.windows=windows
        self.tyres=tyres
        self.engine=engine

    # here self is used because we want to use it in this method
    def self_driving(self,engine):
        print("The car type is {} engine ".format(engine))


car1=Car(4,4,"petrol")
print("The no of tyres in object car1 is {}".format(car1.tyres))
print("The no of windows in object car1 is {}".format(car1.windows))
car1.self_driving("electric")


        