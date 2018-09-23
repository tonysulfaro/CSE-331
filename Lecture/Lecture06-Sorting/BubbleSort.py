def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def Bubble(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if (A[j] < A[j-1]):
                A[j],A[j-1] = A[j-1],A[j]
                #swap(A,j,j-1)





A=[2,100,89,45,68,90,17,29,34,17]
B=[2,100,89,45]
C=[10,9,8,7,6]
Bubble(C)
print(B)