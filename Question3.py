#Code:
one= 0
two= 1
n= int(input("Enter the number of terms:"))
for i in range(n):
    print(one,end=',')
    new= one
    one= two
    two = new + two
#Output:
#Enter the number of terms:10
#0,1,1,2,3,5,8,13,21,34,
