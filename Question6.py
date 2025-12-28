#Code:
lst = list(map(float,input("Enter list:").split()))
print(f"Your list:{lst}")
if lst ==[]:
    print("Empty list!")
else:
    countT=0
    suM= 0
    for i in lst:
        suM += i
        countT += 1
    mean = suM/countT
    lst2 = []  # deviated list
    for i in lst:
        a = (i - mean)**2
        lst2.append(a)
    suM2= 0
    for i in lst2:
        suM2+=i
    avg = suM2/countT
    final = (avg)**(1/2)
    print(f'standrd deviation of given list of elements is {final}')
#Output:
#Enter list:1 2 3 4 5 6
#Your list:[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
#standrd deviation of given list of elements is 1.707825127659933
