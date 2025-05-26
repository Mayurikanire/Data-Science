#1. find the length of a string without using the len() function

# s = input('enter the string')
# counter = 0
# for i in s:
#     counter+=1
# print('length of string is',counter) 

#2. Extract username from a given email.
#mayurikanire4@gmail.com 
# s = input('enter the email')
# pos = s.index('@')

# print(s[0:pos])

#3. Count the frequency of a particular character in a provided string.

# s = input('enter the email')
# term = input('what would you like to search for')
# counter = 0
# for i in s:
#     if i == term:
#         counter +=1
        
# print('frequency',counter)        

#4. write a program which can remove a particular character from a string.
# s = input('enter the string')
# term = input('what would you like to remove')

# result = ''
# for i in s:
#     if i !=term:
#       result = result + i 
# print(result)

# write a program that can check whether a given string is palindrome or not
#abba
# malayalam
# s= input('Enter the string')
# flag = True
# for i in range(0,len(s)//2):
#     if s[i] != s[len(s) - i -1]:
#         flag = False
#         print('Not a palindrome')
#         break
# if flag:
#     print('palindrome')    

# count the no. of words without using split function

# s= input('Enter the string')
# temp = ''
# for i in s:
#     if i !='':
#         temp = temp + i 
#     else:
#         L.append(temp)
#         temp = ' '
# L.append(temp)        
# print(L)        

# write a python program to convert a string to title case without using the title()
# s= input('Enter the string')
# L = []
# for i in s.split():
#     L.append(i[0].upper()+i[1:].lower()) 
# print(" ".join(L))    

# Write a program that can convert an integer to string.

# number = int(input('Enter the number'))
# digits ='0123456789'
# while number !=0:
#     result = digits[number % 10] + result
#     number = number//10
# print(result)
    
    
 #WEEK 1 TASK SOLUTION
 
#  Q.1 print the given string as per stated format
#"Data""Science""Mentorship""Program"
# "By" "CampusX"
# print("Data","Science","Mentorship","Program",sep='-',end='-started-')
# print("By","CampusX",sep='-')

#Q.2 WRITE A PROGRAM THAT WILL CONVERT CELSIUS VALUE TO FAHRENHEIT.
# celsius = float(input('enter the temp in celsius'))

# faren = celsius*(9/5) + 32

# print(faren,'F')

# Q.3 TAKE 2 NUMBERS AS INPUT FROM THE USER WRITE A PROGRAM TOSWAP THE NUMBERS WITHOUT USING ANY SPECIAL PYTHON SYNTAX

# a = 3
# b = 5
# temp = a 
# a =b
# b = temp
# print(a)
# print(b)

#Q.4  write a program to find the euclidean distance between two coordinates. take both coordinates from the user as input.

