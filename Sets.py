# Sets
# A set is an unordered collection of items.
# CHARACTERISTICS -
# Unordered
# Mutable (can be changed)
# No Duplicates
# Can't contain mutable data types

# Creating Sets
# s =set()
# print(s)
# print(type(s))

# # 1D and 2D
# s1 ={1,2,3}
# print(s1)

# #homo and hetro
# s3 = {1,'hello',4.5,(True)}
# print(s3)

# # using type conversion
# s4 = set([1,2,3])
# print(s4)

# # duplicates not allowed
# s5 = {1,2,2,3,3,4}
# print(s5)

# # set cant have mutable items
# # s6 = {1,2,[3,4]}
# # print(s6)

# s1 = {1,2,3}
# s2 = {2,3,1}
# print(s1==s2)

# Accessing Items
# s1 = {1,2,3,4}  does not work in set

#Editing items
# s1 = {1,2,3,4} does not allowed

# Adding items
# s = {1,2,3,4}
# s.add(5) #add
# print(s)

# s.update([5,6,7]) #update
# print(s)

# # Deleting
# s = {1,2,3,4,5}
# print(s)
# # del s 
# # print(s)

# #Discard
# s.discard(4)
# print(s)

# #Remove
# s.remove(5)
# print(s)

#Pop
# s.pop( )
# clear
# s.clear()
# print(s)

# Set Operation
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# #Union(|)
# s1 | s2
# #Intersection(&)
# s1 & s2
# #Difference(-)
# s1 - s2
# s2 -s1
# #Symmetric Difference(^)
# s1 ^ s2
# # Membership test
# 1 not in s1
# # ITeration
# for i in s1:
#     print(i)

#len/sum/min/max/sorted
# s = {3,1,4,5,2,7}
# len(s)
# sum(s)
# min(s)
# max(s)
# sorted(s)

# Union/Update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1.union(s2)

# s1.update(s2)
# print(s1)
# print(s2)

#Intersection/Intersection_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1.intersection(s2)

# s1.intersection_update(s2)
# print(s1)
# print(s2)

#difference/difference_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1.difference(s2)

# s1.difference_update(s2)
# print(s1)
# print(s2)

# isdisjoint/isubset/issuperset
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}

# s1.isdisjoint(s2)

# Frozenset
# frozenset is an immutable version of a python set object
fs = frozenset([1,2,3])
print(fs)

# set comprehension
# {i for i in range(1,11) if i>5}