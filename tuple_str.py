list1 = [[10,20,30],
         [40,50,60],
         [70,80,33]]

sum = 0

for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i == j:
            sum += list1[i][j]

print(sum)

sum = 0

for i in range(len(list1)):
    for j in range(len(list1[i])):
        if i == len(list1) - 1 - i:
            sum += list1[i][j]

print(sum)

# ------------------------------------------

# Tuple --- Ordered, Allow Duplicates, Immutable (Not Changeble)

tup1 = ()
print(type(tup1))   # <class 'tuple'>

tup1 = (10,90.89,"Ashneer")

print(tup1[2])

print(tup1.count(90.89))   # 1
print(tup1.index("Ashneer"))   # 2


tup1 = list(tup1)   # Constructor list

list1 = [10,20,30,40,50]
list2 = [100,20,30,40,50]

tup1.extend(list1)
tup1.extend(list2)

print(tuple(tup1))   # (10, 90.89, 'Ashneer', 10, 20, 30, 40, 50, 100, 20, 30, 40, 50)


tup1 = (10,20)
print(id(tup1))
print(id(tup1))
tup2 = (10,20)
tup1 = tup1+tup2
print(id(tup1))
print(tup1)


tup10 = ((10,20,30),(30,40,50),(50,60,70,30))


list1 = [10,20,30,40,50,61]

list2 = [i for i in list1 if i % 2 == 0]
print(list2)

square = [i**3 for i in list1 if i % 2 == 0]
print(square)

# [(10,1000), (20,8000), (30,27000)...]


jkl = [10,20,30,40,50,60]

ans1= [(i,k) for i in jkl for k in jkl]
print(ans1)
# counter = 0
# for i in jkl:   # 10
#     for k in jkl:   # 10,20,30,40,50,60
#         counter+=1


# print(counter)   # 36

# [(10, 10), (10, 20), (10, 30), (10, 40), (10, 50), (10, 60), (20, 10), (20, 20), (20, 30), (20, 40), (20, 50), (20, 60), (30, 10), (30, 20), (30, 30), (30, 40), (30, 50), (30, 60), (40, 10), (40, 20), (40, 30), (40, 40), (40, 50), (40, 60), (50, 10), (50, 20), (50, 30), (50, 40), (50, 50), (50, 60), (60, 10), (60, 20), (60, 30), (60, 40), (60, 50), (60, 60)]


'''
Tasks in tuple -: 

1. Python program to find the size of a tuple
-> tuple = ("python", "includehelp", 43, 54.23)

2. Python program for adding a Tuple to List and Vice-Versa
-> tuple = ("python", "includehelp", 43, 54.23)

3. Python program to find the maximum and minimum K elements in a tuple
-> 
Input: 
myTuple = (4, 2, 5,7, 1, 8, 9), k = 2

Output: 
(9, 8) , (1, 2)

4. Python program to create a list of tuples from given list having number and its cube in each tuple
->
Input: 
list = [4, 1, 6, 2]

Output: 
[(4, 64), (1, 1), (6, 216), (2, 8)]

5. Python program to remove all tuples of length K
-> 
Input:
[(1, 4), (2), (4,5,6,8), (26), (3, 0, 1), (4)] k = 1

Output:
[(1, 4), (4, 5, 6, 8), (3, 0, 1)]

6. Python program to extract digits from tuple list
->
Input: 
list = [(4, 62), (2, 65), (5, 9), (0,1)]

Output:
[4, 6, 2, 5, 9, 0, 1]

7. Python program to find all pairs combination of two tuples
->
Input:
tup1 = (1, 2), tup2 = (5, 7)

Output:
[(1, 5), (1, 7), (2, 5), (2, 7), (5, 1), (5, 2), (7, 1), (7, 2)]

8. Python program to join tuples if similar initial element
->
Input:
list = [(1, 4), (3, 1), (1, 2), (4, 2), (3, 5)]

Output:
list = [(1, 4, 2), (3, 1, 5), (4, 2)]






9. Python program to sort a list of tuples by second item
->
Input:
[(2, 5), (9, 1), (4, 6), (2, 8), (1, 7)]

Output:
[(9, 1), (2, 5), (4, 6), (1, 7), (2, 8)]

10. Python program to sort a list of tuples in increasing order by the last element in each tuple
-> tupList =[(5, 7), (12, 4), (20, 13), (45, 2)]

11. Python program to sort tuples by frequency of their absolute difference
-> 
Input:
[(4,6), (1, 3), (6, 8), (4, 1), (5, 2)]

Output:
[(4, 1), (5, 2), (4, 6), (1, 3), (6, 8)]

12. Python program to remove duplicate tuples irrespective of order
->
Input:
tupList = [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4), (9, 2)]

Output:
[(1, 2), (5, 7), (4, 6), (2, 9)]

13. Python program to order tuples by list
->
Input:
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

Output:
[('l', 5), ('a', 1), ('k', 2), ('e', 6)]

14. Python program to concatenate maximum tuples
->
Input:
tupList = [("python", 7), ("learn" , 1), ("programming", 7), ("code" , 3)]

Output:
"python programming"

15. Python program to flatten tuple of lists to a tuple
->
Input:
([4, 9, 1], [5 ,6])

Output:
(4, 9, 1, 5, 6)
'''

set1 = {10,20,30,40}

for i in set1:
    print(i)