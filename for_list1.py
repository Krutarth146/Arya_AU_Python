# for(i=0;i<=5;i++)
# {
#     printf("%d",i);
# }

for arya in range(10):
    print(arya,end=' ')   # start - 0, End = 9 (n-1)

print()
for _ in range(25,33):
    print(_,end=' ')  # 25 26 27 28 29 30 31 32

print()
for h in range(25,100,2):   # (start, end (n-1), step(n-1))
    print(h,end=' ')  # 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99

print()
for g in range(100,25,2):
    print(g,end=' ')   # blank

# print()
for w in range(125,90,-3):
    print(w)

for q in range(8,-2,3):
    print(q)   # blank


# for d in range(-6, 5, 2):
#     print(d)

for e in range(3):   # 0 1 2   e = 1
    for c in range(3):  # 0 1 2    c = 2
        if e == c:   # 
            continue    
        print(c,end=' ')   # 1 2 0 2 0 1


# List -------------------------

# array1 = [10,20,30,40,50] -> Same Datatypes


list1 = [10, 90.88, True, 45+9j, "A", "Arya", [10,20,30], (30,40,50), {10,10,102,30,10}, {"Name" : "Krutarth", "Roll" : 5687, 23 : 89.89}]

print(list1)  # [10, 90.88, True, (45+9j), 'A', 'Arya', [10, 20, 30], (30, 40, 50), {10, 102, 30}, {'Name': 'Krutarth', 'Roll': 5687, 23: 89.89}]

print(type(list1))  # <class 'list'>

print(len(list1))  # 10 -> Length start from 1, Index starts from 0

print(list1.__sizeof__())  # 120
print(id(list1))   # 1882587411648   # Reference or Id

list2 = [10,20,30,40]
list1 += list2

print(list1)  # [10, 90.88, True, (45+9j), 'A', 'Arya', [10, 20, 30], (30, 40, 50), {10, 102, 30}, {'Name': 'Krutarth', 'Roll': 5687, 23: 89.89}, 10, 20, 30, 40]


list3 = [10,20,30,40,50,50,60,70,870]

# List -> Allow Duplicates, Ordered (Indexed), Mutable (Chengeble)

# Indexing 

print(list3[0])  # 10
print(list3[-9])  # 10


# Slicing

list3 = [10,20,30,40,50,50,60,70,870]
print(list3[3 : 8])  # [40, 50, 50, 60, 70]
print(list3[13 : 8])  # blank

x = list3[0:3]
print(type(x))

print(list3[2:])  # [30, 40, 50, 50, 60, 70, 870]
print(list3[:5])  # [10, 20, 30, 40, 50]
print(list3[:])  # [10,20,30,40,50,50,60,70,870]
print(list3[:-3])  # [10, 20, 30, 40, 50, 50]

list3 = [10,20,30,40,50,50,60,70,870]
print(list3[2:9:2])  # [30, 50, 60, 870]
print(list3[9:2:2])  # blank
print(list3[9:2:])  # blank
print(list3[3::])  # [40, 50, 50, 60, 70, 870]
print(list3[:-5:])  # [10, 20, 30, 40]
print(list3[:5:-2])  # [870, 60]

print(list3[-2:-6:-2])  # [70, 50]
print(list3[:-6:-2])  # [870, 60, 50]
print(list3[::-1])  # [870, 70, 60, 50, 50, 40, 30, 20, 10]
print(list3[-3:4:2])  # []


# List Methods

list3 = [10,20,30,40,50,50,40,60,70,870]

print(list3.index(40,4))  # 6
# print(list3.append(900))  # None

list3.append(900)
print(list3)  # [10, 20, 30, 40, 50, 50, 40, 60, 70, 870, 900]

list3.extend('900')
print(list3)  # [10, 20, 30, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0']


list4 = [20,30,40,50,60]

# list3.append(list4)
# print(list3)  # [10, 20, 30, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', [20, 30, 40, 50, 60]]

# list3.extend(list4)
# print(list3)  # [10, 20, 30, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', 20, 30, 40, 50, 60]

# list3.insert(3,456)
# print(list3)  # [10, 20, 30, 456, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', 20, 30, 40, 50, 60]

# list3[3] = 800
# print(list3)  # [10, 20, 30, 800, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', 20, 30, 40, 50, 60]

# list3.insert(-1,9000)
# print(list3)   # [10, 20, 30, 800, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', 20, 30, 40, 50, 9000, 60]

# list3.pop()
# print(list3)  # [10, 20, 30, 800, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', 20, 30, 40, 50, 9000]

# list3.pop(3)  # [10, 20, 30, 800, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', 20, 30, 40, 50, 9000]

# list3.remove(9000)
# print(list3)  # [10, 20, 30, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', 20, 30, 40, 50]

list5 = list3.copy()   # shallow Copy

list6 = list3  # Deep Copy

list3.append(300)
print(list5)  # [10, 20, 30, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0']
print(list6)  # [10, 20, 30, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', 300]

list6.append(2000)
print(list3)  # [10, 20, 30, 40, 50, 50, 40, 60, 70, 870, 900, '9', '0', '0', 300, 2000]

del list2

print(list3.count(20))   # 1
list3.reverse()   # 1
print(list3)  # [2000, 300, '0', '0', '9', 900, 870, 70, 60, 40, 50, 50, 40, 30, 20, 10]


list3 = [2000, 300, 900, 870, 70, 60, 40, 50, 50, 40, 30, 20, 10]
list3.sort()
print(list3)  # [10, 20, 30, 40, 40, 50, 50, 60, 70, 300, 870, 900, 2000]

list3.sort(reverse=True)
print(list3)  # [2000, 900, 870, 300, 70, 60, 50, 50, 40, 40, 30, 20, 10]

for i in list3:
    print(i)

for j in range(len(list3)): # 13
    print(list3[j])

list2 = [[10,20,30], [40,50,60]]

for i in list2:
    for j in i: 
        print(j,end=' ')
    print()

# 10 20 30
# 40 50 60

list6 = [[10,20,30],[40,50,60],[70,80,91]]
new = []

for t in list6:
    for w in t:
        if w % 2 != 0:
            new.append(w)

print(new)  # [91]


list6 = [[10,20,30],[40,50,60],[70,80,91]]


# List Comprehension
new1 = [q for g in list6 for q in g if q % 2 != 0]
print(new1)  # [91]

# Task
list6 = [[10,20,30],
         [40,50,60],
         [70,80,91]]

# Task 1-  10 20 30 60 50 40 70 80 91

# Task 2-  1. 10 + 50 + 91 = ?    2. 30 + 50 + 70 = ?

# Task 3- 10 20 30 60 91 80 70 40 50

# Task -4 List Comprehension

ans = []
# matrix = []

# for i in range(3):
#     for j in range(3):
#         matrix.append(int(input()))

# print(matrix)


dim = int(input("ENter Dimensions: "))
# list9 = []
# matrix = []

# for i in range(3):
#     list9 = []
#     for i in range(3):
#         x = int(input())
#         list9.append(x)
#     matrix.append(list9)

# print(matrix)
matrix1 = []

for i in range(dim):
    matrix1.append([int(j) for j in input().split()])

print(matrix1)  # [[10, 20, 30], [20, 40, 66], [88, 33, 2]]