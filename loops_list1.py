# Prime, Perfect, Twin numbers, LCM, HCM, Binary Search, Linear Search

# Prime NUmbers

# 23 -> 1, 23
# 24 -> 1,2,3,4,6,8,12,24
# 29 -> 1, 29
# 44 -> 1,2,4,11,22,44
# 53 -> 1, 53 
counter = 0

i = 2
num = 23
while i<num:    # 1 to 24
    if num % i == 0:
        print(i)
        break
    print(i)
    i+=1   # i = i + 1

print()
# print(counter)

if num == i:
    print(num,"is Prime")
else:
    print("Not Prime")

# Code -> Optimize 1. Time Complexity   2. Space Complexity


num = 0

if num > 0:
    print("Positive")
elif num ==0:
    print("Zero")
else:
    print("Negative")


num1 = 90
num2 = 3400
num3 = 560

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is MAx")
    else:
        print(f"{num3} is Max")
else:
    if num2 > num3:
        print(f"{num2} is Max")
    else:
        print(f"{num3} is Max")

# One Linear 


print(num1 if num1 > num2 else num2)   # Implement


# Linear search

array1 = [10,20,30,40,2,5,2,1,90]
search = int(input())

for i in array1:
    # print(i)
    if search == i:
        print(f"{search} is Found")
        break

if search in array1:      # Membership Operator
    print(f"{search} is Found")