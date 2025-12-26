#breaking statement -> break , continue ,pass
#break -> it will terminate the loop 
#continue -> it will skip current itiration and move to next itiration
#break -> wap to print all even no from 1 to 10 

for i in range(1,11):
    if i % 2 == 0:
        print("it is even ", i)

#wap to print all even number form 1 to 10
for i in range(1,11):
    if i % 2 == 0:
        print("it is even ", i)

numbers = [1,2,3,4,5,6,7]
i=0

while i< len(numbers):
    print(f"Checking: {numbers [i]}")
    if numbers [i] == 5:
        print("5 found: terminating loop.")
        break
    
    #the break statement exist the loop imeditaley 
text = "hello wolrd"

for char in text:
    #check if the character is 'o':
    if char =='o':
        continue #skip the character and move to the next iteration
    print(char, end ="")

#wap to print fibonasie series of a number 5 using for loop 
#wap to print prime numbers from 1 to 100 using for loop 

#list comprenhension
#syntax -> expression for item in iterablel without if condition
#wap to print square of numbers from 1 to 10 using list comphrension
#syntax -> expression for item in iterable without if condition
#wap to print square of numbers from 1 to 10 using list comprehension
a1 = [a**2 for a in range(1, 11)]
print(type(a1))
print(a1)

#syntax -> [expression for item iiterable if condition] with if condition  
a2 = [a**2 for a in range(0,11) if a%2==0]
print(type(a2))
print(a2)

#using list comprehension print which day is today in a week

days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
today = input("enter today day: ").strip().lower()
result = [day for day in days if day == today]
print(result)

for day in days:
    if day == today:
        print(day)

import datetime
#inbuild function deatetime , datetime now
print(datetime.datetime.now())
#%a -> full day name 
print(datetime.datetime.now().strftime("%A"))
# _>else => for
days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
print(datetime.datetime.now().strftime("%A"))
result = [day for day in days if day == today]
print(result)

for i in range(5):
    print(i)
else:
    print("loop finished")

def college_name():
    print("hello kist")

college_name()
college_name()
college_name()
college_name()


#function with parameters
#windsurf refactor \ explain \ generate decoding

def add_return(a,b):
    return a+b
print(add_return (1,22))
print(add_return (0,62))

#function with return type and no parameters
def add_return ():
    print("h1")
    return 1+1

print(add_return())
print(add_return())
 
#function parameter types in python
#1. positional arguments
#2. keyword arguements
#3. variable length aqrguments -> "args" -> tuple
#4. variable length keyword arguments ->  **kwargs -> dictionary

#1. positional arguments
def abc(age, name):
    print("my name is (name), age is (age)")    
abc(27,"SUPAJ")
abc("supaj", 20)

#2. keyword arguements
def ka(age, name):
    print("my name is (name), age is (age)")    
ka(age=20, name="SUPAJ")
ka(name="supaj", age=20)

#3. variable length aqrguments -> "args" -> tuple
