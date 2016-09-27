import sys
def matrixChain(p,n):
    T = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(1,n):
        T[i][i] = 0
    for l in range(2,n):
        for i in range(1,n-l+1):
            j = i + l -1
            T[i][j] = sys.maxsize
            for k in range(i, j):
                q = T[i][k] + T[k+1][j] + p[i-1]*p[k]*p[j]
                if q < T[i][j]:
                    T[i][j] = q
    return T[1][n-1]

#test case
arr = [1, 2, 3 ,4]
size = len(arr)

print("Minimum number of multiplications is",matrixChain(arr, size))