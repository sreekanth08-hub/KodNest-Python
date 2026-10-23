# Function overloading means define multiple functions with same name but different parameters

# Example
def add(a,b):
    return a+b 
def add(a,b,c):
    return a+b+c 
def add(a,b,c,d):
    return a+b+c+d 
print(add(1,2))
print(add(1,2,3)) #Type erro
 