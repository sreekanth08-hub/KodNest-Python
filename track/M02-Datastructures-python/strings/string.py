str="sreekanth"
print(str)
str2='''Sreekanth''' 
print(str2) 
str3="""This is the three double couted string"""
print(str3)  
print("My name is\"sreekanth\" and i am from \'tirupati\' ")


s="  Kodnest Technologies 123  "
print("Originsl String:",s) 

#Case conversion methods 
print("Upper():",s.upper()) #  KODNEST TECHNOLOGIES 123  
print("Lower():",s.lower()) #  kodnest technologies 123 
print("Capitalize():",s.capitalize()) #  Kodnest technologies 123 
print("Title():",s.title()) # Kodnest Technologies 123 
print("swapcase():",s.swapcase()) # kODNEST tECHNOLOGIES 123 

#Searching & counting 
print("find('Tech'):",s.find('Tech')) # 10, returns the index of the "T" 
print("count():",s.count('e')) # 3 ,count of the "e" 


#Replace 
print("Replace('123' to '2025):",s.replace("123","2025"))



# startswith()
#endswith()
#split 
#join 
#isalpha()
#isalnum()
#isspace()
#isdigit()
#islower()
#isupper()  
