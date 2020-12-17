#Maciej Sudol 303073
#Elektronika AGH 3 rok

import random

#wyznacznik macierzy wygenerowanej losowo:
def generate_equal_matrix(N):
    matrix = [[random.randint(0, 10) for x in range(N)] for y in range(N)]
    return matrix

matrixA =generate_equal_matrix(2)
print("Macierz A = ",matrixA)

def return_determinant(A):
    for i in range(0,len(A)):
        max1=abs(A[i][i])
        max2 =i
        for x in range(i+1,len(A)):
            if(abs(A[x][i])>max1):
                max1=abs(A[x][i])
                max2=x
        for x in range(i,len(A)):
            temp=A[max2][x]
            A[max2][x]= A[i][x]
            A[i][x]=temp
        for x in range(i+1,len(A)):
            d=-A[x][i]/A[i][i]
            for j in range(i,len(A)):
                if(i==j):
                    A[x][j] =0
                else:
                    A[x][j]+=d*A[i][j]
    det = 1
    for i in range(0, len(A)):
        det *= A[i][i]
    return det


print("Wyznacznik macierzy A =",return_determinant(matrixA))


