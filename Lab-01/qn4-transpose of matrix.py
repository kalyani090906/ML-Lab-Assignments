def transpose(matrix):
    transpose=[]
    for j in range(len(matrix[0])):
        row=[]
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transpose.append(row)
    return transpose    

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []

print("Enter the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

result = transpose(matrix)
for row in result:
    print(row)