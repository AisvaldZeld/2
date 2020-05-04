A = []
B = []
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(6)
    A.append(temp)
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(4)
    B.append(temp)

print(A)
print(B)

def Matrix(a, b):
    D = []
    counter = 0
    for i in range(len(a[0])):
        temp = []
        for j in range(len(b)):
            temp.append(0)
        D.append(temp)
    print(D)
    if len(a) != len(b[0]):
        return "Разная длина матриц"
    else:
        for i in range(len(D)):
            for j in range(len(D[0])):
                for k in range(len(D)):
                    D[i][j] = a[i][k] * b[k][j]
                    counter = counter + D[i][j]
                D[i][j] = counter
                counter = 0
    return D
print(Matrix(A, B))





