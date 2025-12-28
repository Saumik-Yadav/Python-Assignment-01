#Code: 
n= int(input("Enter your number:"))
for i in range(1,n+1):
    if (i%3==0 and i%5==0):
        print("fizzbuzz")
    elif (i%5==0):
        print("buzz")
    elif (i%3==0):
        print("fizz")
    else:
        print(i)
#Output:
#Enter your number:15
#1
#2
#fizz
#4
#buzz
#fizz
#7
#8
#fizz
#buzz
#11
#fizz
#13
#14
#fizzbuzz
