def minEdit(A,B):
    m = len(A)
    n = len(B)
    L = [[None]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j] = i+j
            elif A[i-1] != B[j-1]:
                L[i][j] =  min(L[i-1][j], L[i][j-1],L[i-1][j-1]) + 1
            else:
                L[i][j] = L[i-1][j-1]
    return L[m][n]

#test case
str1 = "tuesday"
str2 = "thursday"
print("Minimum edit distance is ",minEdit(str1, str2))