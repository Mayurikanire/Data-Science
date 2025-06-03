# What are Lists
#  List is a data type whwre you can store multiple items under 1 name.More tecnically, lists act like dynamic arrays which means you can add more items on the fly.
# L= [20,'Jessa',35.75,[30,60,90]]

#Array Vs Lists
# Memory
# speed of execution
# fixedvs dynamic size
# convenience

# L = [1,2,3]

# print(id(L))
# print(id(L[0]))
# print(id(L[1]))
# print(id(L[2]))
# print(id(1))
# print(id(2))
# print(id(3))

# # CHARASTERISTIS
# Ordered
# changeble/mutable
# Heterogeneous
# can have duplicates
# are dynamic
# can be nested
# items can be accessed
# can contain any kind of objects in python 

# L = [1,2,3]
# L1 = [3,2,1]

# L == L1  #False

# CREATING A LIST

# Empty
# print([])
# 1D /Homogeneous 
# print([1,2,3,4,5])
# 2D
# print([1,2,3,[4,5]])
# 3D 
# print([[[1,2],[3,4]] ,[[5,6],[7,8]]])
# Hetrogenous
# print([1,True,5.6,5+6j,'Hello'])
# Using type conversion
# print(list('Hello'))

# Accessing Items from a List
#Indexing
# L=[1,2,3,[4,5]]
# print(L[-1][-2]) #Negative
# print(L[3])  # Positive

# Slicing
# L = [1,2,3,4,5,6]
# print(L[0:3])
# print(L[0::2])

# ADDING ITEMS TO A LIST
# append  (Add single item at the end)
# L = [1,2,3,4,5]  
# L.append(6)
# print(L)

# Extend (Add multiple items)
# L = [1,2,3,4,5]  
# L.extend([6,7,8])
# print(L)
 
# Insert (Add at index no.)
# L = [1,2,3,4,5]  
# L.insert(1,100)
# print(L)

# EDITING ITEMS IN A LIST
# L = [1,2,3,4,5]
# editing with indexing  
# L[-1] = 500 
# editing with slicing
# L[1:4] = [200,300,400]
# print(L)

# DELETING ITEMS FROM A LIST
# del
# L = [1,2,3,4,5]
#indexing
# del L[-1] 
#slicing
# del L[1:3]
# print(L)

# remove
# L = [1,2,3,4,5]
# L.remove(5)
# print(L)

# pop
# L = [1,2,3,4,5]
# L.pop(3)
# print(L)

# clear
# L = [1,2,3,4,5]
# L.clear()
# print(L)

# OPERATIONS ON LISTS
# Arithmetic
# Membership
# Loop


# Arithmetic (+,*)

# L1 = [1,2,3,4]
# L2 = [5,6,7,8]
#Merge
# print(L1+L2)

# print(L1*3)

# Membership
# L1 = [1,2,3,4,5]
# L2 = [1,2,3,4,[5,6]]

# print(5 in L1)
# print([5,6] not in L2)

# Loop
# L1 = [1,2,3,4,5]
# L2 = [1,2,3,4,[5,6]]
# for i in L1:
#    print(i) 

# LIST FUNCTIONS
# len/min/max/sorted
# L = [2,1,5,7,0]
# print(len(L))
# print(min(L))
# print(max(L))
# print(sorted(L))

# count
# L = [1,2,1,3,4,1,5]
# L.count(5)

# index
# L = [1,2,1,3,4,1,5]
# L.index(2)

# reverse
# L = [1,2,1,3,4,1,5]
# permanently reverses the list 
# L.reverse()
# print(L)

# copy ->shallow
# L = [2,1,5,7,0]
# print(L)
# print(id(L))
# L1 = L.copy()
# print(L1)
# print(id(L1)) 

# LIST COMPREHENSION

#list comprehension provides a concise way of creating lists
#newlist = [expression for item in iterable if condition == True]

# Advantages :
# More time and space efficient than loops
#Require few lines of code
#Transform iterative statement into a formula

# Add 1 to 10 numbers to a list
# L = []

# for i in range(1,11):
#     L.append(i)
# print(L)    

# L = [i for i in range(1,11)]
# print(L)

# scalar multiplication on a vector
# v = [2,3,4]
# s = -3 
#[-6,-9,-12]
# [s*i for i in v]

# Add squares
# L = [1,2,3,4,5]
# [i**2 for i in L]

# print all numbers divisible by 5 in the range of 1 to 50
# [i for i in range(1,51)if i%5 == 0]

# find languages which start with letter p
# languages = ['java','python','php','c','javascript']

# [language for language in languages if language.startswith('p')]

# Nested if with List comprehension 
# basket = ['apple','guava','cherry','banana']
# my_fruits = ['apple','kiwi','grapes','banana']

# add new list from my_friuts and items if the fruit exists in basket and also starts with 'a'

# [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a' )]

# print a (3,3) matrix using list comprehension-> Nested list 
# [[i*j for i in range(1,4)] for j in range(1,4)]

# cartesian products -> List comprehension on 2 lists together

# L1 = [1,2,3,4]
# L2 = [5,6,7,8]
 
# [i*j for i in L1 for j in L2] 

# 2 WAYS TO TRAVERSE A LIST
# -ITEMWISE
# -INDEXWISE

# itemwise
# L =[1,2,3,4]
# for i in L:
#     print(i)
    
# indexwise
# L =[1,2,3,4]
# for i  in range(0,len(L)):
#     print(i)  

# ZIP
# The zip()function returns a zip object,which is an iterator of tuples where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together,
# If the passed iterator have different lengths,the iterator with the least items decides the length of the new iterator. 

# write a program to add items of 2 lists indexwise
# L1 = [1,2,3,4]
# L2 = [-1,-2,-3,-4]

# list(zip(L1,L2))

# [i+j for i,j in zip(L1,L2 )]