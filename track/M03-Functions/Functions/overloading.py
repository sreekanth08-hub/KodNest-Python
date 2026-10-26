# Function overloading means define multiple functions with same name but different parameters

# Example
def add(a,b):
    return a+b 
def add(a,b,c):
    return a+b+c 
def add(a,b,c,d):
    return a+b+c+d 
print(add(1,2)) # missing 2 required positional arguments: 'c' and 'd'
print(add(1,2,3)) # missing 1 required positional arguments: 'd'
print(add(1,2,3,4)) # 10 as output 

# Function overloading is not supported in Python. It Takes most number of arguments. 

# Example using *args 
def add(*args):
    return sum(args)
print(add(1,2)) # 3 as output
print(add(1,2,3)) # 6 as output
print(add(1,2,3,4)) # 10 as output

# using Default arguments 
def add(a,b,c=0):
    return a+b+c 
print(add(1,2))   # 3 as output 
print(add(1,2,3)) # 6 as output