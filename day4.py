#condition  -> if , else , elif, instead of switch is match
#if -> if the condition is true then it runs or go inside its body 
#wap to check if given number is even 
number1 = 3
if(number1 %2 ==0):
    print("its even")
else:
    print("its odd number")
    
#wap to check if given number is odd using if statement only ?
number2 = 3
if(number2 %2 !=0):
    print("its odd")
    
#wap to check if given grade falls in which A,B,C,D,F using if else ?
#this is exam

marks = 45
if(marks >=80 and marks <=100):
    print("its a") 
if(marks >=60 and marks <=79):
    print("its b")
if(marks >=40 and marks <=59):
    print("its c")
else:
    print("failed")
    
#wap to print the given letter is vowel 
#aeiou vowels
vowel1 = "b"
if(vowel1 == "a" or vowel1 =="e" or vowel1 == "i" or vowel1 == "o" or vowel1 =="u"):
    print("its vowel")
else:
    print("its not vowel")
    
    
    
#match -> similar to switch cases 

vowel2 = "b"
match(vowel2):
    case "a":
        print("its vowel")
    case "e":
        print("its vowel")
    case "i":
        print("its vowel")
    case "o":
        print("its vowel")
    case "u":
        print("its vowel")
    case default:
        print("its not vowel")

#wap using match to check if given number is negative, postive or zero 
#given number is negative, positive or zero 

num1 = 10
match(num1):
    case num1 if num1 >= 0:
        print("its positive")
    case num1 if num1 <0:
        print("its negative")
    case default:
        print("its zero")
        
        
#loops -> 
#for , while
#data type -> boolean , range(o,n-1,)
print(range(0,10))
for i in range (0,11):
    print(i)
    
#wap using for loop to check if the given number is odd or even
for i in range (0,11):
    if i%2 ==0:
        print("its even", i)
    else:
        print("its odd", i)
        
#while loops -> 
#initialize the value 
a=0
#while -> condition 
while (a<=10):
    #inc/dec
    if a%2 ==0:
        print("its even", a)
    else:
        print("its odd", a)
    a+=1
    
#wap to print the multiplication table of 7 
for i in range (0,11):
    print("table of (i)")
    for j in range (0,11):
        print(f"{i} * {j} = {i*j}")

#wap to print 
#*
#**
#***
#****
#*****

row=5
for i in range (1, row+1):
    print("*" * i) 
    
#or 

for i in range (0,6):
    for j in range(i):
        print("*" , end="")
        print()
