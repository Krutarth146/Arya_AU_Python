# Code Usability

# 1. Func. Defination
# 2. FUnc. Calling


# Func. Types
# 1. w/o return type and w/o args
# 2. with return type and w/o args
# 3. w/o return type and with args
# 4. with return type and with args

print()

def Arya():
    print(3+200)

Arya()  # 203

# 2. with return type and w/o args

def func1():
    return 21+34

print(func1())   # 55

# 3. w/o return type and with args

def _Ahm(a,b,c,d,e):
    print(a,b,c,d,e)

_Ahm("A",42,32.90,[10,20], {10,20,10})   # A 42 32.9 [10, 20] {10, 20}


def sum(a,c,d=0,e=0):   # dafault Function
    print(a+c+d+e)

sum(10,20,30)   # 60

def royal(k,p,*kru,m=None):
    print(kru)
    for i in kru:
        print(i)

    print(m)

royal(10,20,"vcsdv",11,2,3,4,5,5)


# 4. with return type and with args
list1 = [10,33,56,67,8,8]

def Chair(list10):
    return [i for i in list10 if i % 2 != 0]

print(Chair(list1))  # [33, 67]


list_with_index = [10,20,30,40,50]

for i in enumerate(list_with_index,100):   # To give index to the given list or tuple
    print(i)

for i,j in enumerate(list_with_index,100):   # To give index to the given list or tuple
    print(i,j,sep= '   ')


# 100    10
# 101    20
# 102    30
# 103    40
# 104    50

list1 = [10,20,40,450]
list4 = ["Arya", "Manoj", "Jenil", 'Shrey']

for i,j in zip(list1, list4):
    print(j,i)


def Patel():
    for i in range(5):
        yield i
    else:
        print("Royal is Good")
    
    
for i in Patel():
    print(i)

# Lambda, Map, reduce, Filter, kwargs

print(ord("Z"))
print(chr(122))

set_of_strings = ["Manoj", "Ashok", "Reena"]

string_map_22 = map(lambda my_string: my_string + '_2022', set_of_strings)
set_of_strings_22 = set(string_map_22)
print(set_of_strings_22)

import numpy as np

# salaries = [10000,20000,30000,400,9000]
def get_log_value(salary: int):
    # return np.log(salary)
    print(type(salary))
# log_salaries = list(map(get_log_value, salaries))

get_log_value("Manoj")