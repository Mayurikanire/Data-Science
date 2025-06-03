# TUPLES 
# A tuple in python is similar to a list.The differance between the two is that we cannot
# change the elements2of a tuple once it is assigned whereas we can change elements of a list.
    
# CHARASTERISTICS 
# Ordered
# Unchangeble
# Allows duplicate
    
# Creating Tuple 
t1 =()
# single item tuple    
t2 = ('hello',)
print(t2)
# homogeneous
t3 =(1,2,3,4)
print(t3)
# hetero
t4 =(1,2.5,True,[1,2,3])
print(t4)
# tuple
t5 =(1,2,3,(4,5))
# type conversion
t6 = tuple('hello')

#ACCESSING ITEMS
t3 =(1,2,3,4)
print(t3) #indexing
print(t3[0])
print(t3[-1])

print(t3[0:4:2])#slicing

# Operations on tuple
t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1 + t2)

print(t1*2)
1 in t1
for i in t1:
    print(i)

#Tuple Functions
t =(1,2,3,4)
len(t)
sum(t)
min(t)
max(t)
sorted(t)
t.count(50)
t.index(4)

# Difference betn lists and tuples
# syntax
# mutability
# Speed
# Memory
# built in functionality
# error prone
# usability

# Special syntax
a,b,c = (1,2,3)
print(a,b,c)

a = 1
b = 2
a,b = b,a 
print(a,b)

a,b,*others = (1,2,3,4)
print(a,b)
print(others)

# zipping tuples
a = (1,2,3,4)
b = (5,6,7,8)

tuple(zip(a,b))
