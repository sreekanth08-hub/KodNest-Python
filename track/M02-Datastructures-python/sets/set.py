# #Sets are unorderd, unindexed and mutable, unchageable 
# # Don't support dupllicate values 

# s={1,2,3,4,5}

# # print(s,s[1]) # we cannot access elements using indexing 
# # s[2]=300 # Sets are immutable 

# s.add(7) #adds element to the set
# s.update({8,9}) #adds multiple elements in the set

# s.remove(10) # removes element if present in the set otherwise throughs error
# s.discored(10) # removes element if present in the set otherwise doesn't through error 
# s.pop # removes random element form the set 
# s.clear # clear the set elements 
# # del s # deleted from the memory we cannot access later



# #Frozen Set 
# fs=([1,2,3,]) # once we decalre we cannot add or remove elements in the set
# print(fs, type(fs)) # gives outputs as frozenset
# fs.add(6) # gives error because frozenset is immutable



#More methods in sets

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1.union(set2)) # {1,2,3,4,5,6,7,8} combines all elements
print(set1 | set2) # {1,2,3,4,5,6,7,8}
print(set1.intersection(set2)) # {4,5} common elements in both sets
print(set1 & set2) # {4,5}

print(set1.isdisjoint(set2)) # True if no common elements
print(set1.issuperset(set2)) # True if set1 elements are there in set2 and vise versa
print(set1.issubset(set2)) # True if set1 elements are in set2

print(set1.union(set2)) # {1, 2, 3, 4,5,6,7,8}
print(set1.difference(set2)) # {1,2,3}
print(set1 - set2) # {1,2,3}
print(set2.difference(set1)) # {6,7,8}
print(set2 - set1) # {6,7,8}
print(set1.symmetric_difference(set2)) # {1,2,3,6,7,8}
print(set1 ^ set2) # {1,2,3,6,7,8}

set1.add(6)
print(set1) # {1,2,3,4,5,6}

print(set1) # {1,2,3,4,5,6}

set1.remove(6)
print(set1) # {1,2,3,4,5}

set1.discard(6)
print(set1) # {1,2,3,4,5}

set1.pop()
print(set1) # {1,2,3,4,5,7}

set1.clear() # {}
print(set1, len(set1)) # {} 0