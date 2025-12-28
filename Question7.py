#Code:
print("For 1st matrix:")
row1 = int(input("Enter number of rows: "))
col1 = int(input("Enter number of columns: "))
mat1 = [list(map(int, input(f"Enter row {i+1}: ").split())) for i in range(row1)]
print(mat1)
print("For 2nd matrix:")
row2 = int(input("enter number of romws:"))
col2 = int(input("enter number of columns:"))
mat2 = [list(map(int,input(f"Enter row {i+1}:").split())) for i in range(row2)]
print(mat2)
mat3= []
if (row1 != row2) or (col1!= col2):
    print("Matrix addition is not possible! due to uneven rows or columns!")
else:
    for i in range(row1):
        row = []
        for j in range(col1):
            row.append(mat1[i][j] + mat2[i][j])
        mat3.append(row)
    print("your required matrix:")
    print(mat3)
#Output:
#For 1st matrix:
#Enter number of rows: 2
#Enter number of columns: 2
#Enter row 1: 1 2
#Enter row 2: 3 4
#[[1, 2], [3, 4]]
#For 2nd matrix:
#enter number of romws:2
#enter number of columns:2
#Enter row 1:1 2
#Enter row 2:3 4
#[[1, 2], [3, 4]]
#your required matrix:
#[[2, 4], [6, 8]]
