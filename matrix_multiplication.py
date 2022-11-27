def matrix_create():
    matrix = []
    j = 0
    for j in range(3):
        new_row = []
        for i in range(3):
            element = input(f"Enter {i}th element of {j}th row: ")
            new_row.append(element)
        matrix.append(new_row)
        j += 1
    return matrix


def multilplier(first_row,sec_matrix,j):
    result = 0
    for i in range(3):
        result += int(first_row[i])*int(sec_matrix[i][j])
    return result

print("Enter the first matrix:-")
first_matrix = matrix_create()
print("Enter the second matrix:-")
second_matrix = matrix_create()


final_matrix = []
for k in range(3):
    new_row = []
    for j in range(3):
        element = multilplier(first_matrix[k],second_matrix,j)
        new_row.append(element)
    final_matrix.append(new_row)
print(final_matrix)
