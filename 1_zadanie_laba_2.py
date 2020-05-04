A = [7, 3, 2, 3, 4, 5, 9, 7, 8, 9, 2]

B = [9, 6, 8, 4, 6, 8, 3, 2, 1, 0, 3]

def Scalar(a, b):
    D = []
    if len(a) != len(b):
        return "Разница рамеров векторов"
    else:
        for i in range(len(a)):
            D.append(A[i] * B[i])
    return D
print(Scalar(A, B))



