#Code:
= int(input("Enter matrix size: "))
if (n!=2 and n!=3):
    print("Error: Only 2x2 or 3x3 matrices are allowed")
else:
    print("enter your elements:")
    matrix = [list(map(int,input(f"Enter row {i+1}:").split())) for i in range(n)]
    print("Your entered matrix is-")
    print(matrix)
    s = 1
    for i in range(n):
        if (len(matrix[i]) != n):
            s = 0
    if (s == 0):
        print("Error: Matrix is not square. Determinant not possible.")
    else:
        if n == 2:
            a, b = matrix[0][0], matrix[0][1]
            c, d = matrix[1][0], matrix[1][1]
            det = a * d - b * c
        else:  
            a, b, c = matrix[0][0], matrix[0][1], matrix[0][2]
            d, e, f = matrix[1][0], matrix[1][1], matrix[1][2]
            g, h, i = matrix[2][0], matrix[2][1], matrix[2][2]
            det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

        print(f"Determinant of the matrix is: {det}")
#Output:
#Enter matrix size: 3
#enter your elements:
#Enter row 1:1 4 6
#Enter row 2:3 5 77
#Enter row 3:3 5 6
#Your entered matrix is-
#[[1, 4, 6], [3, 5, 77], [3, 5, 6]]
#Determinant of the matrix is: 497
