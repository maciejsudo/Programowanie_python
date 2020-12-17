#Maciej Sudol 303073
#Elektronika AGH 3 rok
import random
import numpy as np


def generate_equal_matrix(N):
    matrix = [[random.randint(0, 100) for x in range(N)] for y in range(N)]
    return matrix

def sum_matrix(matrixA,matrixB):
    if(len(matrixA)==len(matrixB)):
        matrixSUM = [[0 for x in range(len(matrixA))] for y in range(len(matrixA))]
        for i in range(0,len(matrixA)):
            for j in range(0,len(matrixA)):
                matrixSUM[i][j]= matrixA[i][j]+matrixB[i][j]
        print(matrixSUM)
    else:
        print("macierze nie są równe")




matrixA=generate_equal_matrix(128)
matrixB=generate_equal_matrix(128)
print(matrixA)
print(matrixB)

sum_matrix(matrixA,matrixB)