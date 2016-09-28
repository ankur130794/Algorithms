def cutRod(price):
    n = len(price)
    length = list(range(0,n+1))
    T = [[0 for _ in range(n+1)] for _ in range(n)]
    for i in range(n):
        for j in range(n+1):
            if j==0:
                T[i][j] = 0
            elif i==0 and j!=0:
                T[i][j] = price[i]*length[j]
            elif length[i+1] > length[j]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j],(price[i] + T[i][j-i-1]))
    return T[n-1][n]

#test case
arr = [1,5,8,9,10,17,17,20]
print(cutRod(arr))