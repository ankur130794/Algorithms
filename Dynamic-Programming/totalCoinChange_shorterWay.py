def coinChange(coins, n): #where n is the required target
    ways = [1] + [0]*n
    for coin in coins:
        for i in range(coin, n+1):
            ways[i] += ways[i - coin]
    return ways[n]

#test case
arr = [1,2,3]
n = 5
print("Total coin change is",coinChange(arr,n))