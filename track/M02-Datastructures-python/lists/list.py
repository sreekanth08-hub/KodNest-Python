# #Creating a list
# numbers=[1,2,3,4,5,3]
# print(numbers)

# # Accessing list items
# print(numbers[3])

# #inserting elements in the list
# numbers.append(6)
# print(numbers)

# print(f"length of list:{len(numbers)}")

# # removing elements from the list
# numbers.pop()
# print(numbers)

# #insert elements using position
# numbers.insert(0,0)
# print(numbers)

# #slicing 
# print(numbers[1:5])

# #updating the list 
# print(numbers)
# numbers[0]=0
# numbers[0:2]=3,4,5
# print(numbers)


# #extend method using adding multiple values 
# numbers.extend((7,8,9))
# print(numbers)

# # clearing the list 
# numbers.clear()
# print(numbers)

# # deleting the list from the file or memory 
# del numbers


# # Sorted the list using sorted function
# x=[3,4,5,7,8,9,2]
# sorted_x=sorted(x)
# print(sorted_x)
# #sorted the list unsing sort function
# numbers=[4.5,1,6,8,7]
# numbers.sort()
# print(numbers)
# # in descending order
# sorted_list=sorted(numbers,reverse=True)
# print(sorted_list)

# checking the list modification in memory using id function 
numbers=[10,20]
print(numbers,id(numbers))
values=numbers 
print(values,id(values))
values=[100,200]
print(values,id(values))
print(numbers,id(numbers))
print(values)
print(numbers)