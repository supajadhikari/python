#wap to add two numbers by asking user about the value of it 
num1=int(input("enter first number: "))
num2=int(input("Enter second number"))
num3=num1+num2
print(type(num1), type(num2))
print(num3)

#type conversion  - > str(),int(), float(), list(), tuple(), set()
num4 = "55"
num5 = int(num4)

#convert num4 to float 
#string methods in python 
#string format -> \', \n
#string methods lower(), upper() , title(), capitalize()
#strip(), join(), find(), replace(), spilit()

name= "hyyy its spj"
print(name.upper())
address = " kist "
print(address.lower())
names = "spj adh"
print(names.capitalize())
print(names.title())

#join
print(names, address.join(names))

#strip -> remove extra space
print(name.strip())

#find -> find index of the character or string 
print(names.find("spj"))

#replace -> replace character in a string 
print(name, name.replace("i","o"))

#split -> it spilits a string into a list 
print(name.split())

#boolean -> isuper, is lower, istitle
print(name.isupper()) #falsee
print(address.islower()) #false
print(names.istitle()) #false

#string indexing and slicing 
name= "hyyy its spj"
names = "spj adh"

#string indexing 0 to n-1
print(names[0])
print(names[3])
print(names[3:5])
print(names[:10])

#string slicing -> start : end : step 
values = "0123456789"
print(values[0:9:2])
print(values[::3])  # :: to show the 3rd character 

#negative indexing 
print(names[-6:-1]) #andar

#string reverse
print(names[::-1])
print(values[9:0:-1])
print(values[3:5])

#wap to print even index character of a string 
sample = "abcdefghiklmnopqrstuvwxyz"
print(sample[::2]) #it prints the second word of index 
print(sample[::-2]) #reverse of the complete letter 

#operators and operands 
#5+5=10

# type of operators 
#1. Arithmetic Operator 
#2. Assignment Operator 
#3. Comparison opeartors
#4. Logical Opeartor
#5. Bit Wise Opeartor 
#6. membership opeartors 
#7. Identify Opeartors

#1. Arithmetic Operator  -> +,-,/,*,//,**,%
print(6+6)
print(6-6)
print(6*6)
print(6/6)
print(6//6)  #floor division return int if both operand are int 
print(6**6) #exponent
print(6%6) # modulus  -> remainder - > 

#2. Assignment Operator  ->  =,+=, *=, /=, %=, //= , **=
a=10
a+=10
print(a)
a-=10
print(a) #10
a*=10
print(a) #100
a/=10
print(a) #10.0
a//=10
print(a) #1.0
a**=2
print(a) #1.0

#3. Comparison opeartors ->  ==, !=, > , < , >=, <=

x=10
y=20
print(x==y) #false
print( x!=y) #true
print( x > y) #false
print( x < y) #true
print( x >= y) #false
print( x<=y) #true

# 4. logical opeartors 
a = True
b = False
print(a and b) #false
print(a or b) #true
print(not a) #false