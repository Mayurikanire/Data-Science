#Lets create a function
def is_even(num):
    """
    This function returns if a given number is odd or even
    input - any valid integer
    output - odd/even
    created on - 5th jun 2025
     
    """
    if type(num) == int:
        if num % 2 == 0:
            return 'even'
        else:
            return 'odd'
    else:
        return 'pagl hai kya'    
# function
# function_name(input)
for i in range(1,11):
    x = is_even(i)
    print(x)
    
# Types of arguments
# Default argument
# Positional argument
# Keyword argument

def power(a=1,b=1):
    return a**b
print(power(2))

# *args and **kwargs
# *args and **kwargs are special python keywords that are used 
# to pass the variable length of arguments to a function

def multiply(*args):
    product = 1
    
    for i in args:
        product = product * i 
    print(args)
    return product
print(multiply(1,2,3,4,5))

# **kwargs 
# keyword arguments mean that they contain a key-value pair, like a python dictionary.
def display(**kwargs):
    for(key,value) in kwargs.items():
        print(key,'->',value)
print(display(india='delhi',srilanka='colombo',nepal='kathmandu'))         

# order of the arguments matter(normaal->*args->**kwargs)
# The words 'args'and'kwargs' are only a convention you can use any name of your choice.

# How functions are executed in memory
