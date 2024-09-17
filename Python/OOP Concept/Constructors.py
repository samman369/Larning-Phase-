# In basic case 
'''
class Car:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    
    def __init__(self, name, brand, model):
        self.name = name
        self.brand = brand
        self.model = model 

audi = Car("audi","new")
print(audi)

# in this case it will not work because second constractor 
# is overriding the first one and it is not calling the first one
'''

# We can make multiple constractor like this 
class Animal:
    def __init__(self,*args):
        if len(args)==1:
            self.name = args[0]
        elif len(args)==2:
            self.name = args[0]
            self.species = args[1]
        elif len(args)==3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    def make_sound(self, sound):
        return "The animal is {} and says {}".format(self.name, sound)

dog=Animal("dog","mammals",17)
print(dog.name)
print(dog.species)
print(dog.age)
print(dog.make_sound("woof wwoof"))