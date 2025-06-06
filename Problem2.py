def knapsack(val,wt,W):
    n=len(val)
    dp=[[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(W+1):
            if wt[i-1]<=w:
                dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][W]

val=[60,100,120]
wt=[10,20,30]
W=50

print(knapsack(val,wt,W))
