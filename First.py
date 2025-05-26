#1. curr_pop = 10000

# for i in range(10,0,-1):
#     print(i,curr_pop)
#     curr_pop = curr_pop/1.1

# 2.Sequence sum
#1/1!+2/2!+3/3!+...

# n = int(input('enter n'))
# result = 0
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
#     result = result + i/fact
# print(result)    

# 3. NESTED LOOPS

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)

# 4.Pattern1
# rows = int(input('enter no. of rows '))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()


# Pattern 2:
# rows = int(input('enter number of rows'))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     for k in range(i-1,0,-1):
#         print(k,end='')
#     print()

# 5.LOOP CONTROL STATEMENT
# BREAK
# CONTINUE
# PASS

# for i in range(1,10):
#     if i==5:
#         break
#     print(i)


#6. FIND PRIME NUMBERS BETN RANGE
# lower = int(input('enter lower range'))
# upper= int(input('enter uppper range'))

# for i in range(lower,upper+1):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         print(i)
    
    
# 7. continue 
# for i in range(1,10):
#     if i ==5:
#         continue
#     print(i)

# 8. Pass table
# for i in range(1,10):
#     pass


# STRINGS
# CREATING STRINGS 

# s = 'hello'
# s = "hello"
# s = '''Hello''' #Multiline strings
# print(s)

# ACCESSING SUBSTRINGS FROM A STRING

# s = 'hello world'
# print(s[3])

#NEGATIVE INDEXING
# s = 'hello world'
# print(s[-1])

#SLICING
# s = 'hello world'
# print(s[::-1])  to  reverse a string 
# print(s[0:5:2]) stepsize

#EDITING AND DELETING STRING

# s = 'Hello World'
# s[0] = 'h'
# python strings are immutable(not changable)

# s = 'Hello World'
# del s 
# print(s)

# OPERATIONS ON STRINGS
# ARITHMETIC OPERATORS
# print('mayu'+ 'ri')
# print('mayuri'*5)
# 'Mumbai' =='Mumbai'
#'mumbai' > 'pune'

# COMMON FUNCTIONS
# len
# max
# min
# sorted

# len('hello world')
# max('hello world')
# min('hello world')
# sorted('hello world',reverse = true)

# s = 'hello world'
# s.capitalize()

# s.title()

# s.upper()

# s.lower()

# s.swapcase()


#COUNT/FIND/INDEX
# 'my name is mayuri'.count('i')
# 'my name is mayuri'.find('is')
# 'my name is mayuri'.index('x')

#ENDSWITH/STARTSWITH
# 'my name is mayuri'.endswith('ri')
# 'my name is mayuri'.startswith('my')

#FORMAT
# name = 'mayuri'
# p = 'student'
# 'Hi my name is {} and i am a{}'.format(name,p)

#ISALNUM/ISALPHA/ISDIGIT/ISIDENTIFIER

# 'mayuri123'.isalnum()
# 'mayuri'.isalpha()
# '123abc'.isdigit()
# 'first_name1'.isidentifier()

# 'hi my name is mayuri'.split()
# " ".join(['hi','my','name','is','mayuri'])

# 'hi my name is mayuri'.replace('mayuri','kanire')

# 'nitish          '.strip( )