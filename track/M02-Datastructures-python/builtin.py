# Sorted Create a list in asc or desc order in new List 
# Sorted Works on List,Tuple,Set,dictionary  

#Ascending_order
marks=[60,73,48,50] 
new_marks=sorted(marks)
print(new_marks)

#Descending_order
marks=[60,73,48,50] 
new_marks=sorted(marks,reverse=True)
print(new_marks)

names={"apple","mango","banana"}
new_names=sorted(names)
print(new_names) 


#Sort()
# .sort sorts the existing list and dont create a newList 
# It uses in List only 

#Ascending_order
marks=[60,73,48,50] 
marks.sort()
print(new_marks)

#Descending_order
marks=[60,73,48,50] 
marks.sort(reverse=True)
print(marks)

names={"apple","mango","banana"}
names.sort()
print(names) #Throws error Because .sort does not works on set



