def lis(arr):
    n = len(arr)
    lis = [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maximum = max(lis)
    return maximum

#test case
arr = [14,32,40,66,21,45,9,6]
print("Length of longest increasing subsequence is ", lis(arr))
