# Functions

# 1. Inbuilt   2. User Defined

# Inbuilt ----> len, min, max, 

# User defined Functions (UDF)

#include<conio.h>

# Arya():   # Func. Defination
#     evde
#     v
#     e
#     rve
#     v
#     erv


# Arya()  # Func. Calling


# Func. Types

# 1. without Return Type and Without Args
# 2. with Return Type and Without Args
# 3. without Return Type and With Args
# 4. with Return Type and With Args


# 1. without Return Type and Without Args

def Arya():
    print("This is Arya Function")

Arya()  # Func. Calling


# 2. with Return Type and Without Args

def royal():
    a,b,c = 90,89,78
    return a*b*c

print(royal())  # 624780

def patel():
    list1 = [10,20,30,40,50]
    tup1 = ((10,20,30), (40,50,60))

    return list1, tup1

x = patel()
print(x)   # ([10,20,30,40,50], ((10,20,30), (40,50,60)))
print(type(x))   # <class 'tuple'>


# 3. without Return Type and With Args

def Jalp(num1,num2 = 34, num3=90):
    print(num1 * num2 // num3)


Jalp(10,80,-91)   # -9


# 4. with Return Type and With Args

def dhiraj_sir(x, y, z):
    print(z)
    return (x+y) * z

print(dhiraj_sir("Kru", "Tarth".lower(), 3))  # KrutarthKrutarthKrutarth


# -----------------------------------------

def demo( *patel, num5 = 78):
    # print(patel)
    print(patel[4])
    print(patel[4][-2][0])
    print(patel[4][-2][0][3])
    print(patel[4][-2][0][3]['address'])
    print(patel[4][-2][0][3]['address']['pincode'])
    print(patel[4][-2][0][3]['address']['pincode'][3])   # 80

    for k in patel:
        print(k)
        print(type(k))

demo(10,20,90.90, "Patel", [[10,20,], [(90,78,67, {"name" : "Arya", 'address' : {"city" : "Ahm", "pincode" : [10,20,90,80,78]}})], []])

# ---------------------------------


# kwargs Next