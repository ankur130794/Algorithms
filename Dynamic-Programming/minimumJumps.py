import sys
def minJumps(arr):
    n = len(arr)
    T = [0]*n
    for i in range(1,n):
        for j in range(0,i):
            if T[i] == 0:
                T[i] = sys.maxsize
            if arr[j]>=i-j:
                T[i] = min(T[i],T[j]+1)
    return T[n-1]

#test case
arr=[1,3,6,1,0,9]
print("The minimum number of jumps are",minJumps(arr))