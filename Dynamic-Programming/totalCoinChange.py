import sys
def coinChange(arr, n):
    m = len(arr)
    T = [[0 for _ in range(m)] for _ in range(n+1)]

    for i in range(m):
        T[0][i] = 1
    for i in range(1, n+1):
        for j in range(m):
            if i>=arr[j]:
                # Number of solutions including arr[j]
                x = T[i - arr[j]][j]
            else:
                x=0
            if j>=1:
                # Number of solutions excluding arr[j]
                y = T[i][j-1]
            else:
                y=0

            # total number
            T[i][j] = x + y

    return T[n][m-1]

# test case
arr = [1, 2, 3]
n = 5
print("Total coin change is",coinChange(arr, n))