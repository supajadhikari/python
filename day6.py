#continue of day 5
#functions
""" 
details()
details(name = "ram", age = "30 ")  """

def var_l(*one):
    print(one)

var_l(1,2,3,4,5)
#4. variable lngth arguments -> args -> tuple

def var_l(a,b,*args):
    print(args)
    print(a,b)
var_l(1,2,3,4,5)

#5. variable legth keyboard arguments -> **kwargs -> dict 
def abcde(**kwargs):
    print(kwargs)

abcde(name = "spj", age ="27")

#Wap to in function to use all parameter type in function,
def all_functions(a,b,c,args,kargs):
    pass
all_functions(10,20,30,40,50,60, name = "spj", age = 20, college = "kist")
print("above is pass keyboard that lets use to skip function - day6.py:28")

#pass

#recursion in python function -> function calling itself

def add(n):
    if n==1:
        return
    else:
       return n + add(n-1)
add(5)

#factorial of number using recusrion 5! = 5*4*3*2*1 = 120

def factorial(n):
    if  n ==0:
        return 1
        return n * factorial(n-1)
print(factorial (5))

#type hinting in python 
def abcr(a:int , b:int)-> int:
    print(a+b)

abcr(0,1)
abcr(10,5,20,5)

#variable name -> lamba parameter  
one = lambda x : x+1
print(one(4))

#global and local variable 
#global -> if we make a variable outside a functions we can use
#if inside a function and outside it 
#local -> variable make inside the functions can be used only 
#inside the functin cannot access outside 

#global and local variable 
global_var = 10
print(global_var) 

def abce():
    local_var =20
    print(local_var)
    print(global_var)

abce()
print(local_var)

#function inside map
list1 = (1,2,3,4,5)
list2 = list(map( lambda x : x*2), list1)
print(list2 )

