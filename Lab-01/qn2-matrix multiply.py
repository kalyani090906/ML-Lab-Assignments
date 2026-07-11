def matrix_mul(A,B):
    if len(A[0]) != len(B):
        return "Matrix can't be multiplied"
    
    result = []

    for i in range(len(A)):
        row=[]
        for j in range(len(B[0])):
            total=0
            for k in range(len(B)):
                total+= A[i][k] *B[k][j]
            row.append(total)
        result.append(row)        

    return result



row1 = int(input("no of rows of A: "))
col1 = int(input("no of col of A: "))

A = []
print("Enter Matrix A:")
for i in range(row1):
    row = list(map(int, input().split()))
    A.append(row)

row2 = int(input("no of rows of B: "))
col2 = int(input("no of col of B: "))

B = []
print("Enter Matrix B:")
for i in range(row2):
    row = list(map(int, input().split()))
    B.append(row)

result = matrix_mul(A, B)
print(result)