#Code: 
actual = list(map(int,input("Enter elements of actual list:").split()))
print("actual values:")
print(actual)
a = 0
for i in actual:
    a+=1
predicted = list(map(int,input("Enter elements of predicted list").split()))
print('predicted values:')
print(predicted)
p = 0
for i in predicted:
    p+=1
if (a != p):
    print("MAE and MSE are not possible due to difference in length")
else:
    n= a  # n denotes number of observations
    Sum = 0
    SuM = 0
    for i in range(n):
        Sum += abs(actual[i] - predicted[i])
        SuM += (actual[i] - predicted[i])**2
    MAE = Sum / n
    MSE = SuM / n
    print(f"MAE = {MAE}")
    print(f"MSE = {MSE}")
#Output:
#Enter elements of actual list:2 4 5 6
#actual values:
#[2, 4, 5, 6]
#Enter elements of predicted list2 5 7 3
#predicted values:
#[2, 5, 7, 3]
#MAE = 1.5
#MSE = 3.5
