# Dictionary
# dictionary in pyhton is a collection of keys values,used to stored data values like a map,
# which ,nlike other data types which hold only a single value as an element.
# dict = {'name':'mayuri'}
#CHARACTERISTICS -
# mutable
# indexing has no meaning
# keys can not be duplicated
# keys can not be mutable items

# empty dictionary
d = {}
print(d)
# 1D dictionary
d1 = {'name':'mayuri','age':'21'}
print(d1)
# mixed keys
d2 = {(1,2,3):1,'hello':'world'}
print(d2)
# 2D dictionary
s = {
    'name':'mayuri',
    'college':'kdk',
    'sem':8,
    'subjects':{
        'dsa':50,
        'maths':82,
        'english':45
    }
}
print(s)
# using sequence and dict function
d4 = dict([(1,1),(2,2),(3,3)])
print(d4)
# duplicate keys
# d5 = {'name':'mayuri','name':'nihal'}
# print(d5)
# mutable items as keys
# d6 = {'name':'mayuri',[1,2,3]:4}

# Accessing items
my_dict = {'name':'Trushali','age':'21'}
# []
my_dict['name']
# get
my_dict.get('age')

# Adding key-value pair
d4['gender'] = 'female'
print(d4)

# pop/del/popitem/clear
# Editing key value pair
s['subjects']['dsa'] = 80
print(s)

# Dictionary Operations
#Membership
print(s)
'mayuri' in s 

d ={'name':'mayuri','gender':'female','age':'21'}
for i in d:
    print(i,d[i])
    
# Dictionary Functions
len(d)  
print(d)
sorted(d,reverse=True)
max(d)

# items/keys/values
print(d)

print(d.items())
print(d.keys())
print(d.values())

# update
d1 = {1:2,3:4,4:5}
d2 = {4:7,6:8}
d1.update(d2)
print(d1)

# Dictionary Comprehension
#{key :value for vars in iterable}

# print 1 to 10 numbers and their squares
print({i:i**2 for i in range(1,11)})

# using existing dict
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print({key:value*0.62 for (key,value) in distances.items()})

days  = ["sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
print({i:j for (i,j) in zip(days,temp_C)})

# using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
print({key:value for (key,value) in products.items()if value>0})

# Nested Comprehension
# print tables of number from 2 to 4
print({i:{j:i*j for j in range(1,11)}for i in range(2,5)})

