class calculator():

def __init__(self,name):
 self.name=name

def add(self,a,b):
 result=a+b
 return result

def sub(self,a,b):
 return=(a-b)

def mul(self,a,b):
 return(a*b)

def div(self,a,b):
 return(a/b)

a=int(input("enter first number:"))
b=int(input("enter second number:"))
obj1=calculator("calculator")
print(obj1.add(a,b))
print(obj1.subtract(a,b))
print(obj1.multiply(a,b))
print(obj1.divide(a,b))
