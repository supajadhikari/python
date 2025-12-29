class calc:
    def __init__(self,n1,n2):
        self.n1 =n1
        self.n2 =n2
    def add(self):
        print(f"add : {self.n1+self.n2}")

    def sub(self):
        print(f"sub : {self.n1-self.n2}")
    
    def div(self):
        print(f"div: {self.n1/self.n2}")

    def mul(self):
        print(f"mul : {self.n1*self.n2}")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
obj1 = calc(num1,num2)

#obj1
obj1.add()
obj1.sub()
obj1.mul()
obj1.div()