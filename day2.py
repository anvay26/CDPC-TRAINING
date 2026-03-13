# Program 1 : Check Even or Odd

# no=int(input("Enter no: "))
# if(no%2==0):
#     print("Even")
# else:
#     print("Odd")

# Example Output
# Enter no: 4
# Even


# Program 2 : Find the Largest of 3 Numbers

# b=0
# for i in range(3):
#     a=int(input("Enter No:"))
#     if(a>b):
#         b=a
# print("Largest no is:",b)

# Example Output
# Enter No:4
# Enter No:3
# Enter No:5
# Largest no is: 5


# Program 3 : Check Positive, Negative, Zero

# a=int(input("Enter No: "))
# if a>0:
#     print("Positive")
# elif a<0:
#     print("Negative")
# else:
#     print("Zero")

# Example Output
# Enter No: -3
# Negative


# Program 4 : Check Divisibility by Both 3 and 5

# a=int(input("Enter No.: "))
# if a%3==0:
#     if a%5==0:
#         print("Divisible by both 3 and 5")
#     else:
#         print("Not Divisible")

# Example Output
# Enter No.: 15
# Divisible by both 3 and 5


# Program 5 : Print Numbers from 1 to N

# n=int(input("Give n: "))
# for i in range(n):
#     print(i+1)

# Example Output
# Give n: 5
# 1
# 2
# 3
# 4
# 5


# Program 6 : Print Even Numbers from 1 to N

# n=int(input("Give n: "))
# for i in range(n):
#     if (i+1)%2==0:
#         print(i+1)

# Example Output
# Give n: 9
# 2
# 4
# 6
# 8


# Program 7 : Sum of First N Natural Numbers

# n=int(input("Enter N: "))
# sum=0
# for i in range(n):
#     sum=sum+i+1
# print("Sum of first N natural numbers is:",sum)

# Example Output
# Enter N: 5
# Sum of first N natural numbers is: 15


# Program 8 : Factorial of a Number

# n=int(input("Enter a number:"))
# sum=1
# while n>0:
#     sum=sum*n
#     n-=1
# print("Factorial is: ", sum)

# Example Output
# Enter a number:5
# Factorial is: 120


# Program 9 : Multiplication Table

# n=int(input("Enter no: "))
# for i in range(1,11):
#     print(n*i)

# Example Output
# Enter no: 5
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50


# Program 10 : Count Digits in a Number

# Method 1

# a=int(input("Enter no: "))
# count=len(str(a))
# print(count)

# Method 2

# a=int(input("Enter no: "))
# count=0
# while a>0:
#     count=count+1
#     a=a//10
# print(count)

# Example Output
# Enter no: 345
# 3


# Program 11 : Reverse a Number

# Method 1

# a=int(input("Enter a no: "))
# rev=0
# while a>0:
#     rem=a%10
#     rev=rev*10 + rem
#     a=a//10
# print(rev)

# Method 2

# a=int(input("Enter a no: "))
# b=int(str(a)[::-1])
# print(b)

# Example Output
# Enter a no: 345
# 543


# Program 12 : Check Palindrome Number

# a=int(input("Enter no: "))
# temp=a
# rev=0
# while a>0:
#     rem=a%10
#     rev=rev*10 + rem
#     a=a//10
# if temp==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Example Output
# Enter no: 121
# Palindrome


# Program 13 : Sum of Digits of a Number

# a=int(input("Enter a no: "))
# sum=0
# while a>0:
#     rem=a%10
#     sum+= rem
#     a=a//10
# print(sum)

# Example Output
# Enter a no: 123
# 6


# Program 14 : Armstrong Number

# a=int(input("Enter a no: "))
# temp=a
# sum=0
# count=0
# while a>0:
#     count=count+1
#     a=a//10
# while a>0:
#     rem=a%10
#     sum+= rem**count
#     a=a//10
# if temp==sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# Example Output
# Enter a no: 153
# Armstrong


# Program 15 : Numbers Divisible by 7 between 1 and N

# n=int(input("Enter N: "))
# for i in range(n):
#     if (i+1)%7==0:
#         print(i+1)

# Example Output
# Enter N: 50
# 7
# 14
# 21
# 28
# 35
# 42
# 49
