t = int(input())
for _ in range(t):
    a = input()
    b = input()
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    length = 0
    index = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    index = i
            else:
                dp[i][j] = 0
    common = a[index - length:index]
    answer = n + m - 2*len(common)
    print(answer)
