from itertools import permutations
def boxStack(arr):
    n = len(arr)
    all = []
    total = []
    for i in range(n):
        all.append(list(permutations(arr[i],3)))
    for i in range(len(all)):
        for j in range(len(all[i])):
            if all[i][j][0] > all[i][j][1]:
                total.append(all[i][j])
    total.sort(key=lambda x: x[0]*x[1])
    total.reverse()
    m = len(total)
    bs = [0 for x in range(m)]
    for i in range(m):
        bs[i] = total[i][2]
    for i in range(1,len(bs)):
        for j in range(0,i):
            if total[i][0] < total[j][0] and total[i][1] < total[j][1]:
                bs[i] = bs[j] + total[i][2]
    return max(bs)
arr=[[4,6,7],[1,2,3],[4,5,6],[10,12,32]]
print(boxStack(arr))
