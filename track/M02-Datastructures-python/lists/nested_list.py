student_marks=[
    [78,85,91],
    [72,88,80],
    [90,84,89]
]
for marks in student_marks:
    for mark in marks:
        print(mark) 

#dictionary containt List 
departments={
    "Development":["Asha","Ravi"],
    "Testing":["Meera","Kiran"]
    }
for department, employees in departments.items():
    print(department)
    for employee in employees:
        print(employee)

# Displaying relared values together 
for department,employees in departments.items():
    for employee in employees:
        print(department,"-",employee)


#Travesing a Dictionary containing dictionaries
students={
    "Asha":{
        "Python":88,
        "SQL":82
    },
    "Ravi":{
        "Python":76,
        "SQL":84
    }
}
for student,subjects in students.items():
    print(student)
    for subject,marks in subjects.items():
        print(subject,"-",marks)
