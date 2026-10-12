squares=[]
for i in range(1,6):
    squares.append(i*i)
print(squares)


square_list=[i*i for i in range(1,11)]
print(square_list)


even=[]
for i in range(1,11):
    if i%2==0:
        even.append(i)
print(even)



even_list=[i for i in range(1,11) if i%2==0]
print(even_list)



names=["Sreekanth","Rahul","Pavan","Naresh"]

new_list=[i.upper() for i in names]
print(new_list)