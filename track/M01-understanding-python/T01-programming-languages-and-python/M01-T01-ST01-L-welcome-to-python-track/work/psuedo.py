# To print Hello world

""" print "Hello world" """

print("Hello World \nThank you for learning python.") #/n  used to print in next line
print("My name is",end =" ") #end="" used to print in the same line if it's two print statments or more
print("I am learning pyhton")




#To find wheather number (n) is even or odd 
"""read n 
if n%2==0
     print "even"
 otherwise
    print "odd" """
n=int(input())
print("Even" if n%2==0 else "Odd")



#To find the number is pos, neg or zero 
"""read number 
    if number>0:
     print "positive"
 otherwise
     print "negative" 
otherwise:
     print "zero" """
if n>0:
    print("Postivie")
elif n<0:
    print("Negative")
else:
    print("Zero")



#To find the largest among 3 numbers a,b,c
"""read a 
read b 
read c 
if a>b and a>c 
    print a 
otherwise 
    b>a and b>c 
    print b 
otherwise 
    print c """


a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
c=int(input("Enter C value:"))
if a>b and a>c:
    print(f"{a} is greater")
elif b>a and b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")
