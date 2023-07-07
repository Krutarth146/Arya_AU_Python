# Single Line Comment

'''
Multi
Line
Comment
'''

# Datatypes -> int
# Variables 

# Python is Dynamic Language, Interpreted Lang. (Line by Line)

_dhiraj_sir = 900

print(_dhiraj_sir)
print(type(_dhiraj_sir))   # <class 'int'>

arya123 = 78.32
print(type(arya123))  # <class 'float'>

_ = "y"
print(type(_))  # <class 'str'>

_1 = "yash"
print(type(_1))  # <class 'str'>

jk = True
print(type(jk))  # <class 'bool'>

patel_1 = 45 + 90j
print(patel_1)   # (45+90j)    # 45 is real part, 90j is Imaginary part

print(45j+patel_1)   # (45+135j)
print(type(patel_1))   # <class 'complex'>


list1 = [10, 67.90, True, "Manoj", 'w', 90+80j, [1,2,3], ((1,2,3),(5,6,7)), {10,20,30,10,20,90,232}, {"name" : "Krutarth", 90:78.89, 'arya_roll':[10,20,340,90]}]

print(list1)  # [10, 67.9, True, 'Manoj', 'w', (90+80j), [1, 2, 3], ((1, 2, 3), (5, 6, 7)), {10, 20, 30}, {'name': 'Krutarth', 90: 78.89, 'arya_roll': [10, 20, 340, 90]}] 

print(type(list1))  # <class 'list'>


# print("""
#     Arya Patel  
#     Sargasan Chokdi
#     Gnr

# """)


# print('Arya Patel',end=' ') 
# print('Good Afternoon')   # Arya Patel Good Afternoon


# x = "Hello"
# y = "Patel"

# print(x,y,sep='\n')   # Hello 
#                      #  Patel

                    
# x = 80
# y = 34

# print(x,"+",y,"=",x+y)  # 80 + 34 = 114

# print(f"{x} + {y} = {x+y}")   # fstring  # 80 + 34 = 114

# -----------------------------------------------------------------------

# Input() and Typecasting

# x = input('Enter your Number: ')
# print(x)   # 46

# print(type(x))  # <class 'str'>

# y = input()   # Int

# print(x+y)   # 4623


# num1 = int(input("ENter Number: "))
# num2 = int(input("ENter Number: "))
# print(num1 + num2)


# Type casting -> one Dt to another Dt
# 1. Implicit Typecasting   2. Explicit Typecasting

x = True  # Bool   # 1
y = 90    # Int    # 90

print(x+y)   # 91   # Implicit Typecasting


h = 90.78
print(int(h))   # 90   # Explicit Typecasting

import math

print(math.floor(90.99))   # 90
print(math.ceil(90.01))   # 91

j = '45'
print(int(j))   # 45

print(type(j))  # str

x = '90.34'
print(int(float(x)))

v = 90
print(float(v))   # 90.0

# Operators ----------------------------------

# Ascii values, Operator Precedence And Associativity



# Arithmetic O/p   + - * / // % **

print(45 + 90 - 23 * 8 / 2)   # 43.0
print(45 + 90 - 92)          # 43


print(51 / 2)   # 25.5 
print(51 // 2)   # 25  (Floor Division)
print(51 % 2)   # 1  (Gives Remainder)


print(-18 // 4)   # -5

print(2 ** 3 ** 2)   # 2 ** 9   -> 512


# Assignment O/p   =  += -= *= /= //= %= <<= >>=  &= |=

x = 90
x+=2   # 92
x%=2   # 0   

print(x)   # 0

# Bitwise o/p   -> Bit by bit convrersion

# & | ^

# AND Table  (A*B)

# i/p  i/p  o/p
# 0     0    0
# 1     0    0
# 0     1    0
# 1     1    1  


# OR Table  (A+B)

# i/p  i/p  o/p
# 0     0    0
# 1     0    1
# 0     1    1
# 1     1    1  


# XOR Table  (Same - 0, Different - 1)

# i/p  i/p  o/p
# 0     0    0
# 1     0    1
# 0     1    1
# 1     1    0  

# Decimal to Binary  56987  2254  11  6321 
# Binary tio Decimal   11101  1111101111  1010

print(ord('A'))   # 65
print(ord('a'))   # 97

print(chr(122))   # z

print(34 & 89)  # 0
print(493 | 12)  # 0
print(493 ^ 12)  # 0
print(493 << 2)  # 0
print(493 >> 3)  # 0


# Take days as Input from user and find Total years, months and Remaining Days
# Take seconds as I/p and find Hours, minutes and remaining seconds

# 400 -> 1 Year, 1 Month, 5 Remaing Days using fstring




str1 = "Madam"
str1 = str1.lower()
str2 = str1[::-1]

if str1 == str2:
    print("same")


# 103  -> 301



# Intialization
# while condition:
    # statements
    # Flow

_ = 1

while _ <= 100:
    print(_,end=' ')
    _+=1


print()
print()
_ = 100

while _ >= 1:
    _-=1  
    # print("Infinite")
    if _ % 5 == 0 and (_ % 7 == 0 or _ % 10 == 0):
        if _ == 50:
            continue
        print(_,end=' ')   # 90 80 70 60 40 35 30 20 10 0



# Palindrome Number
print()

num = 1 # -> 231
rev = 0

safe = num
while num!=0:
    rem = num % 10  # 1
    rev = (rev * 10) + rem  # sum = 231
    num = num // 10   # num = 0

print(rev)  # 151


if safe == rev:   # 0 == 151
    print("Palindrome")

# 1 to 10000 Palindrome Numbers
# Sum of Digits
# Find Power of any nUMber
# Find TOtal Digits of any Number