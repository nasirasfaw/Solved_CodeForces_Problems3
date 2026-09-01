n = int(input())

dp = [0]*(n+1)
if n % 2 != 0:
    dp[n] = 0
else:
    dp[2] = 2
    for i in range(4, n+1):
        dp[i] = dp[i-2]*2

print(dp[n]) 
