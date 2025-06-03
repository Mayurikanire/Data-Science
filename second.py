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

# p1x = int(input('enter x coordinate of 1st point'))
# p1x = int(input('enter y coordinate of 1st point'))
# p2y = int(input('enter x coordinate of 2nd point'))
# p2y = int(input('enter y coordinate of 2nd point'))
# distance - ((p2x - p1x)**2 + (p2y - p1y)**2)**0.5
# print(distance)

# Q.5 Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user
# Hint- si=(p*t*r)/100
# p = int(input('Enter amount'))
# t = int(input('Enter time period'))
# r = float(input('Enter rate'))
# interest =  (p*t*r)/100
# print('The interest is', interest)

# Q.6 Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
#input: heads-4,legs-12
# head = int(input('Enter the no of heads'))
# leg  = int(input('Enter the no of legs'))
 
 
 #Q.7 Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
 # formula = n(n+1)(2n+1)/6
# n = int(input('enter the number'))
 
# result = (n*(n+1)*(2*n+1))/6
# print(result)
 
#Q.8 Given the first 2 terms of an ARITHMETIC SERIES. fIND the Nth term of the series. Assume all inputs are provided by the user.
# an = a+(n-1)d
 
# first_term = int(input('Enter first term'))
# second_term = int(input('Enter second term'))
# n = int(input('enter the value of n')) 
# d = second_term - first_term 
# an = first_term + (n-1)*d
# print(an)

# Q.9 Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denomenator values of the fractions from the user.
# n1 = int(input('num1'))
# d1 = int(input('den1'))
# n2 = int(input('num2'))
# d2 = int(input('den2'))

# rn = n1*d2 + n2*d1
# rd = d1* d2
# print('{}/{}'.format(rn,rd))


#Q.10  Given the height,width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
# Input: Dimension of milk tank 
#H = 20cm,L =20cm,B = 20cm
#Dimensions of glass
#h = 3cm,r = 1cm
# import math
# h_t = float(input('height'))
# b_t = float(input('breadth'))
# l_t = float(input('length'))

# h_g = float(input('height of glass'))
# r_g = float(input('radius of the glass'))
# vol_tank =  h_t*b_t*l_t
# vol_glass = 3.14*r_g*r_g*h_g

# print('no of glasses',math.floor(vol_tank/vol_glass))

# TASK 2
# Q.1 write a program that will give you in hand monthly salary after deduction on CTC-HRA(10%),
#DA(5%),PF(3%)and taxes deduction as below:

# ctc = int(input('Enter your anual CTC:'))

# if ctc <500000:
#     salary=ctc*.82
# elif ctc < 1000000:
#     salary=ctc*.72  
# elif ctc < 2000000:
#     salary=ctc*.62 
# else:
#     salary=ctc*.52
# print("you in hand monthly salary will be-", round(salary/12,2))   

#Q.2 write a program that take a user input of three angles and will find out whether it can form a triangle or not.
#Hint - Sum of all angles is 180 and all angles are positive
# first = int(input('enter the 1st angle'))
# second = int(input('enter the 2nd angle'))
# third= int(input('enter the 3rd angle'))

# if (first+second+third) == 180 and first>0 and second>0 and third>0:
#     print('Forms a triangle')
# else:
#     print('does not form a triangle') 
              
#Q.3 write a program that will take user input of costt price and selling price and determines whether its a loss or a profit.
# cost_price = int(input('Enter cost price-'))
# selling_price = int(input('Enter selling price-'))

# if cost_price < selling_price:
#     print('Profit')
# elif cost_price > selling_price:
#     print('Loss')
# else:
#     print('No Loss No Gain')                      

 #Q.4 Write a menu driven program
menu = input(""" 
Hi select an option
1.cms to ft
2.km to ft
3.USD to INR
4.Exit              
""")

# if menu =='1':
#      float(input('Enter the cm value'))
#      print('ft value is',0.032*cm)
# elif menu =='2':
#     km = float(input('enter the km value'))
#     print('miles value is',km*0.62)
# elif menu =='3':
#     float(input('enter usd'))
#     print('inr',usd*80)
# else:
#     exit()    
        
 
#Q.5 Display Fibonacci series up to 10 terms
    
# num1,num2 = 0,1
# for i in range(10):
#     print(num1)
    
#     next = num1 + num2
    
#     num1 = num2
#     num2 = next

#Q.6 