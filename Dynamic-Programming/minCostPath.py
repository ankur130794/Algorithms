def minCost(cost,m,n): #cost from (0,0) to (m,n)
    R = len(cost)
    C = len(cost[0])
    T = [[0]*C for _ in range(R)]
    T[0][0] = cost[0][0]
    for i in range(1,m+1):
        T[i][0] = T[i-1][0] + cost[i][0]
    for i in range(1,n+1):
        T[0][i] = T[0][i-1] + cost[0][i]
    for i in range(1,m+1):
        for j in range(1,n+1):
            T[i][j] = min(T[i-1][j],T[i][j-1],T[i-1][j-1]) + cost[i][j]
    return T[m][n]

#test case
cost = [[4, 7, 1],
        [3, 2, 9],
        [1, 3, 4]]
print("Minimum cost path is",minCost(cost, 2, 2))