# Tuples are order collection of data and tuples are immutable 
# Tuples are used to store the data to change again and again

#Creating Tuples 

numbers=() #or numbers=tuple()
print(numbers,type(numbers)) #<class 'tuple'>

# methods and in tuples
names=("Alice","Bob","Charlie","Bob")
print(names.count("Bob"))
print(names.index("Alice"))
print(names[3])   # Bob
print(names[-1])  # Bob
y=names[0:3] 
print(y,type(y)) # ("Alice","Bob","Charlie") ,tuple



# Packing and unpacking tuples 
a="sreekanth"
age=20
language="Pyhton"
details=a,age,language 
print(details,type(details))  # ("sreekanth",20,"Pyhton") ,tuple

#unpacking tuple
fruits=("Apple","Banana","Cherry")
f1,f2,f3=fruits
print(f1)
print(f2)
print(f3)