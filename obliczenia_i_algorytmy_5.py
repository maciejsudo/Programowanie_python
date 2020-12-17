#Maciej Sudol 303073
#Elektronika AGH 3 rok

import random



def generate_equal_matrix(N):
    matrix = [[random.randint(0, 100) for x in range(N)] for y in range(N)]
    return matrix

def mult_matrix(matrixA,matrixB):
    if(len(matrixA)==len(matrixB)):
        matrixMULT = [[0 for x in range(len(matrixA))] for y in range(len(matrixA))]
        for i in range(len(matrixA)):
            for j in range(len(matrixA)):
                for k in range (len(matrixA)):
                    matrixMULT[i][j] += matrixA[i][k]*matrixB[k][j]
        print(matrixMULT)
    else:
        print("macierze nie są równe")


matrixA=generate_equal_matrix(8)
print(matrixA)

matrixB=generate_equal_matrix(8)
print(matrixB)

mult_matrix(matrixA,matrixB)