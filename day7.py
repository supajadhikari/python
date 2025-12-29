# oop - object oriented programming 
# class -obj ,4 pillers , methods
# class - classname:
# #methods , constructor , properties
#class - blue print
#object - instance of class  
class student:
    name = "sagar"
    age = 80
    
    #dender methods/magic methods
    #_init_
    def __init__(self, name="sagar", age=80):
        print("nothing to print::")
        self.name = name
        self.age = age

    def details(self):
        return f"name: {self.name}, age: {self.age}"

student1 = student()
print(student1.name, student1.age)
print(student1.details())
student2 = student("shyam", 25)
print(student2.name, student2.age) 

#wap using oop to have a class name kist and properties like building classes , teacher and other your wish.
class kist:
    building_class = "A"
    teacher = "Mr. John"
    subject = "Mathematics"

    def __init__(self, building_class="A", teacher="Mr. John", subject="Mathematics"):
        self.building_class = building_class
        self.teacher = teacher
        self.subject = subject

    def class_details(self):
        return f"Class: {self.building_class}, Teacher: {self.teacher}, Subject: {self.subject}"
kist1 = kist()

#make a functionable calculator using oop ask 2 inputs from user and need to have add sub multiply divide methods divide part

class calculator:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def div(self):
        return self.num1 / self.num2
    def multiply(self):
        return self.num1 * self.num2

num1 = int(input("enter a number: "))
num2 = int(input("enter another number: ")) 

calc = calculator(num1,num2)
print("Addition:", calc.add())
print("Subtraction:", calc.sub())
print("Division:", calc.div())
print("Multiplication:", calc.multiply())

#methods of oop

# 3 types of methods in python oop
#1. instance methods -> need object to 
#2. class methods -> can call this type of method directly from class name 
#3. static method -> independent

class kist:
    def __init__(self , building  , classes):
        self.building = building
        self.classes = classes
    
    def details(self,a,b):
        print(a+b, self.building)

#class methods
@classmethod
def class_method(cls,a,b):
    print(a+b)
kist.class_method(5,3)
obj1 = kist("building 1 ", "20")
obj1.details(5,6)

#static method

@staticmethod

def static_meth(a,b):
    print(a+b)
kist.static_meth(5,8)
obj1 = kist("bulding1", "20")
obj1.details(5,7)
