#absctraction
#wap using absctraction for different shapes area calculation -> shape 
#ABC -> area -> circle , rectangle , square 

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class square(shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
square = square(4)
print("Area of square: ", square.area())
Circle = Circle(5)
print("Area of circle: ", Circle.area()) 


#Polymorphism -> having many forms::
#human -> animal -> dog,cat, etc..
#polymorphismm::

class animal:
    def walk(self):
        print("Animal is walking")
    def fly(self):
        print("animal is flying")
        
class human(animal):
    def walk(self):
        print("human is  walking on two legs")
    def fly(self):
        print("human cannot fly")
        
class bird(animal):
    def fly(self):
        print("animal is flying")
    def fly(self):
        print("bird can fly")

class dog(animal):
    def walk(self):
        print("animal is walking on 4 legs")
    def fly(self):
        print("dog cannot fly")
        
animal = [human(), bird(), dog(),]

for a in animal:
    a.walk()
    a.fly()
    
#error handling in python -> try , except , else , finally 
print("program started")
try:
    a = 10/0
    print(a)
    
except ZeroDivisionError as ERROR:
    print("ERROR ")
    
except Exception as e: 
    print("something went wrong: ")
    
else:
    print("not getting any error ")
    
finally:
    print("program error end here: ")
    print("program ended")
    
