def binomialCoeff(n , k):

    T = [0 for _ in range(k+1)]
    T[0] = 1
    for i in range(1,n+1):
        #computing pascal triangle
        j = min(i ,k)
        while (j>0):
            T[j] = T[j] + T[j-1]
            j -= 1
    return T[k]

#test case
n = 5
k = 2
print(binomialCoeff(n,k))