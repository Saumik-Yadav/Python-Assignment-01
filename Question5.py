#Code:
lst = list(map(float, input("Enter numbers:").split()))
print(f'given list:{lst}')
if (lst==[]):
    print("Empty list!")
else:
    Sum=0
    countT= 0
    #mean:-
    for i in lst:
        Sum= Sum + i
        countT+= 1
    mean = Sum/countT
    print(f'mean:{mean}')
    #sorting
    for i in range(0,countT-1):
        for j in range(i+1,countT):
            if (lst[i]>lst[j]):
                a = lst[j]
                lst[j] = lst[i]
                lst[i] = a
    print(f'sorted list:{lst}')
    #median:-
    if (countT%2 == 0):
        median= ((lst[int(countT/2)] + lst[int(countT/2-1)]))/2
    else:
        median = lst[int((countT-1)/2)]
    print(f'median:{median}')
    #Mode:-
    D = {}
    for i in lst:
        if (i in D):
            D[i]+=1
        else:
            D[i] =1
    maX = 0
    mode = 0
    for key,value in D.items():
        if (value >maX):
            maX = value
            mode = key
    if (maX == 1):
        print("NO mode!")
    else:
        print(f'mode:{mode}')
#Output:
#Enter numbers:1 3 5 7 9 2 4 6 8 3 4 3
#given list:[1.0, 3.0, 5.0, 7.0, 9.0, 2.0, 4.0, 6.0, 8.0, 3.0, 4.0, 3.0]
#mean:4.583333333333333
#sorted list:[1.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
#median:4.0
#mode:3.0
