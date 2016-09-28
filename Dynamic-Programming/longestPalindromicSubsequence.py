def lps(str):
    n = len(str)
    T = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        T[i][i] = 1

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if str[i] == str[j] and l == 2:
                T[i][j] = 2
            elif str[i] == str[j]:
                T[i][j] = T[i+1][j-1] + 2
            else:
                T[i][j] = max(T[i][j-1], T[i+1][j]);

    return T[0][n-1]

#test case
str = "ACECCBA"
print("The length of the LPS is",lps(str))