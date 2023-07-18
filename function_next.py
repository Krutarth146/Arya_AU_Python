def Arya(num1,*kru, num3 = 90):
    print(kru)   # (20, 30, [10, 20, 30], (20, 90))
    print(type(kru))   # <class 'tuple'>

    for k in kru:
        print(k)

    print(len(kru))


Arya(10,20,30,[10,20,30], (20,90))   # (10, 20, 30, [10, 20, 30], (20, 90))


# kwargs

# DIctionary Type

def Patel(*args, **kwargs):
    ''' Kwargs '''
    print(kwargs)   # {'name': 'Arya', 'disease': 'Stomach', 'type': 'Bacteria'}
    print(type(kwargs))   # <class 'dict'>
    print(kwargs['''name'''])

    for k in kwargs:
        print(k)

        
    for k in kwargs.keys():
        print(k)
        
    for k in kwargs.values():
        print(k)

    
    for key, val in kwargs.items():
        print(key,'----->' ,val)

    print(args)

    

Patel(10, 90, "Arya", name = 'Arya', disease = 'Stomach', type = 'Bacteria')
# print(Patel.__doc__)  # Kwargs


# -------------------------------------

range1 = int(input("Enter the Number : "))

def example(x):
    for i in range(1,x+1):
        # print(i,end=' ')
        yield i

print(example(5))   # <generator object example at 0x0000019C7B579A10>

x = example(range1)
# print(example(range1).__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

for i in example(range1):
    print(i)
