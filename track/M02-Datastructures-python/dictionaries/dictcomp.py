cities=["Bengaluru", "Pune", "bengaluru", "Chennai","Pune"]
unique_cities={city.lower() for city in cities}
print(unique_cities)

numbers=[2,3,2,4,5]
unique_squares={number*number for number in numbers}
print(unique_squares) 

#dictionary Comprehension
#Noramal Code
numbers=[2,3,4,5]
cube_by_numbers={}
for number in numbers:
    cube_by_numbers[number]=number**3 
    print(cube_by_numbers)
# Using dict comphrension
cube_by_numbers={number:number**3 for number in numbers}
print(cube_by_numbers)