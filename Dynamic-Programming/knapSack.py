def knapSack(W, wt, val):
    n = len(val)
    T = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                T[i][w] = 0
            elif wt[i-1] <= w:
                T[i][w] = max(val[i-1] + T[i-1][w-wt[i-1]],  T[i-1][w])
            else:
                T[i][w] = T[i-1][w]

    return T[n][W]

# test case
val = [1,4,5,7]
wt = [1,3,4,5]
W = 7
print(knapSack(W, wt, val))
