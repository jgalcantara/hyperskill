import numpy


def menu():
    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    choice_ = int(input("Your choice: "))
    return choice_


def size(string):
    row, column = input(string).split()
    return int(row), int(column)


def mat_format(string, row):
    print(string)
    matrix = [[int(i) if "." not in i else float(i) for i in input().split()] for _ in range(int(row))]
    return matrix


def mat_add():
    rx1, cx1 = size("Enter size of first matrix: ")
    matrix_x1 = mat_format("Enter first matrix:", rx1)
    rx2, cx2 = size("Enter size of second matrix: ")
    matrix_x2 = mat_format("Enter second matrix:", rx2)
    if rx1 == rx2 and cx1 == cx2:
        mat = [[float(matrix_x1[i][j]) + float(matrix_x2[i][j]) for j in range(int(cx1))] for i in range(int(rx1))]
        print("The result is:")
        for i in range(int(rx1)):
            print(*mat[i], sep=" ")
    else:
        print("The operation cannot be performed.")
    return True


def mat_mulc():
    rx1, cx1 = size("Enter size of matrix: ")
    matrix_x1 = mat_format("Enter matrix:", rx1)
    consx = float(input("Enter constant: "))
    mat = [[float(matrix_x1[i][j]) * consx for j in range(int(cx1))] for i in range(int(rx1))]
    print("The result is:")
    for i in range(int(rx1)):
        print(*mat[i], sep=" ")
    return True


def mat_mulm():
    rx1, cx1 = size("Enter size of first matrix: ")
    matrix_x1 = mat_format("Enter first matrix:", rx1)
    rx2, cx2 = size("Enter size of second matrix: ")
    matrix_x2 = mat_format("Enter second matrix:", rx2)
    if cx1 == rx2:
        matrix = []
        for i in range(int(rx1)):
            matrix.append([])
            for j in range(int(cx2)):
                total = 0
                for k in range(int(rx2)):
                    total += float(matrix_x1[i][k]) * float(matrix_x2[k][j])
                matrix[i].append(total)
        print("The result is:")
        for i in range(int(rx1)):
            print(*matrix[i], sep=" ")
    else:
        print("The operation cannot be performed.")
    return True


def mat_trans():
    print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    select = int(input("Your choice: "))
    if select == 1:
        rx1, cx1 = size("Enter matrix size: ")
        matrix_x1 = mat_format("Enter matrix:", rx1)
        matrix_x1_t = []
        for i in range(int(cx1)):
            matrix_x1_t.append([])
            for j in range(int(rx1)):
                matrix_x1_t[i].append(matrix_x1[j][i])
        print("The result is:")
        for i in range(int(cx1)):
            print(*matrix_x1_t[i], sep=" ")
    elif select == 2:
        rx1, cx1 = size("Enter matrix size: ")
        matrix_x1 = mat_format("Enter matrix:", rx1)
        matrix_x1_t = []
        i = 0
        for j in range(int(cx1) - 1, -1, -1):
            matrix_x1_t.append([])
            for k in range(int(rx1) - 1, -1, -1):
                matrix_x1_t[i].append(matrix_x1[k][j])
            i += 1
        print("The result is:")
        for i in range(int(cx1)):
            print(*matrix_x1_t[i], sep=" ")
    elif select == 3:
        rx1, cx1 = size("Enter matrix size: ")
        matrix_x1 = mat_format("Enter matrix:", rx1)
        matrix_x1_t = []
        for i in range(int(rx1)):
            matrix_x1_t.append([])
            for j in range(int(cx1) - 1, -1, -1):
                matrix_x1_t[i].append(matrix_x1[i][j])
        print("The result is:")
        for i in range(int(cx1)):
            print(*matrix_x1_t[i], sep=" ")
    elif select == 4:
        rx1, cx1 = size("Enter matrix size: ")
        matrix_x1 = mat_format("Enter matrix:", rx1)
        matrix_x1_t = []
        k = 0
        for j in range(int(cx1) - 1, -1, -1):
            matrix_x1_t.append([])
            for i in range(int(rx1)):
                matrix_x1_t[k].append(matrix_x1[j][i])
            k += 1
        print("The result is:")
        for i in range(int(cx1)):
            print(*matrix_x1_t[i], sep=" ")


def mat_det(num):
    rx1, cx1 = size("Enter matrix size: ")
    matrix_x1 = mat_format("Enter matrix:", rx1)
    if rx1 == cx1 and num == 1:
        print(mat_def_recur(matrix_x1))
    elif rx1 == cx1 and num == 2:
        det = mat_def_recur(matrix_x1)
        if det == 0:
            print("This matrix doesn't have an inverse.")
        else:
            mat_inv(matrix_x1, rx1, cx1)
    else:
        print("The operation cannot be performed.")
    return True


def mat_def_recur(matrix):
    total = 0
    if len(matrix) == 1:
        total = matrix[0][0]
    elif len(matrix) == 2:
        total = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    else:
        for i in range(len(matrix)):
            copy = matrix[1:]
            for j in range(len(copy)):
                copy[j] = copy[j][0:i] + copy[j][i + 1:]
            cof = (-1) ** (i % 2)
            sub_det = mat_def_recur(copy)
            total += cof * matrix[0][i] * sub_det
    return total

def mat_inv(matrix, rows, columns):
    x = matrix
    inv = numpy.linalg.inv(x)
    mat = [[round(inv[i][j], 3) for j in range(int(columns))] for i in range(int(rows))]
    print("The result is:")
    for i in range(int(rows)):
        print(*mat[i], sep=" ")
    return True


while True:
    choice = menu()
    if choice == 1:
        mat_add()
    elif choice == 2:
        mat_mulc()
    elif choice == 3:
        mat_mulm()
    elif choice == 4:
        mat_trans()
    elif choice == 5:
        mat_det(1)
    elif choice == 6:
        mat_det(2)
    elif choice == 0:
        exit()