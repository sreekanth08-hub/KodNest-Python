# A Function Is a Resuable block of code that performs a specific task 
# We define Function using def Keyword 
def greeting():
    print("Welcome to python")
greeting() #calling the function # Welcome to python as output 

# Local Variables 
# A Local variable is variable created inside a function. It can normally be accessed only with that function 
def student():
    name="Ravi"
    age=22 
    print(name) # name is accessible here 
#print(name) # name is not accessible here because it is outside the function 

student()  


#Golabal Variable 
# A golabal variable is a variable declared outside a all functions.It can be accessed by inside function 
college="KodNest"
def display():
    print(college) # KodNest as output 
print(college)
display() 

x=100
def demo():
    x=50
    print(x) # 100 as output
demo()
print(x) # 100 as output 
