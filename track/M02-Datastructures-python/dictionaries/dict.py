# {key:value}, mutable, key cannot be duplicate

student = {
    "name" : "Amit",
    "age" : 21,
    "course" : "Computer Science",
    "Tech" : ["Computer Science", "Python", "SQL"]
}

student["age"] = 25
student.update({"cgpa" : 8.5})
print(student["age"])
print(student, type(student), len(student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("cgpa"))

print(student.pop("course"))
student.popitem() # last item
student.clear() # remove all items
del student
# print(student)

student = {
    "name" : "Rahul",
    "age" : 23,
    "Tech" : ["Python", "SQL"]
}

student.setdefault("age", 22) #set default add the key vlaue if not there
print(student)

keys = ["name", "age", "course"]
y = 0

student = dict.fromkeys(keys, y) # returns dictionary with keys from keys and value from y 
print(student)

my_dict = student.copy() # returns copy of the dictionary 
print(my_dict)
my_dict.update({"name" : "amit"}) # updates the dictionary
print(my_dict)



for i in student.keys(): # returns keys of the dictionary 
    print(i)
for j in student.values(): # returns values of the dictionary 
    print(j)
for k,j in student.items(): # returns key and values of the dictionary 
    print(k,j)


#Nested Loopings

students={
    "stu1":{
        "name":"Rahul",
        "age" : 23,
        "Tech" : ["Computer Science", "Python", "SQL"]
    },
    "stu2":{
        "name":"sri",
        "age" : 23,
        "Tech" : ["Computer Science", "Java", "SQLite"]
    }
}
for x in students:
    print(x)
    for y in students[x]:
        print(y,students[x][y])
    
# dict lookup 
list_products=[101,102,103,104]
products={
    "P101":["Keyboard",1200],
    "P102":["Mouse",600],
    "P103":["Monitor",8500]
}
print(products["P103"]) #direct lookup : Access value in dict o(1)
res=products.get("P103","Product Not Found") # safe lookup 



