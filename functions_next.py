# with Return type And With Args.

def Arya(num):
    for i in range(1,num+1):
        return i

print(Arya(5))   # 1


def Arya(num):
    for i in range(1,num+1):
        yield i

# print(Arya(5))   # <generator object Arya at 0x0000020560299A10>

for i in Arya(5):
    print(i,end=' ')   # 1 2 3 4 5

print()
x = Arya(5)
print(x.__next__())  # 1
print(x.__next__())  # 2
print(x.__next__())  # 3


# ----------------------------------

# lambda (Anounomous Function)

def square(num):
    return num ** 2


print(square(5))   # 25


# ------------------------------
def cube(num1):
    return num1 ** 3

print(cube(6))  # 216

cube_l = lambda num1 : num1 ** 3


print(type(cube_l))   # <class 'function'>

print(cube_l(7))  # 343


arya = lambda x,y = 25 : y + x**2 

print(arya(20))   # 425


# Quadratic Func  ---> (a*x*x) + (b*x) + c

def quadratic(a1,b1,c1):
    return lambda x : (a1*x*x) + (b1*x) + c1

patel = quadratic(10,20,30)

print(patel(5))  # 250 + 100 + 30  ---> 380


# Nested Lambda

royal = lambda x : lambda g,k : g+k+x

techno = royal(5)

print(techno(30,10))   # 45


# ---------------------------------
royal = lambda x,y = 10 : lambda g,k : g+k+x+y
print(royal(25)(22,90))  # 147


# --------------------------------------------------


def square(num):
    return num ** 2

lst2 = [10,90,45,33,22]

res = []

for i in lst2:
    res.append(square(i))

print(res)  # [100, 8100, 2025, 1089, 484]


# Powerful Functions  -----> Map, Reduce, Filter

x = list(map(lambda num : num ** 2, lst2))


lst2 = [10,90,45,33,22]
y = tuple(map(lambda x : x+500, lst2))
# print(x)   # <map object at 0x000001CA884B7BB0>
print(y)   # (510, 590, 545, 533, 522)