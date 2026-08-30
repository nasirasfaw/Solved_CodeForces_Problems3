t = int(input())
for _ in range(t):
    n = int(input())

    coins = [2**k for k in range(1, n+1)]

    c1 = coins[:n//2 - 1] + [coins[n-1]]
    c2 = coins[n//2 - 1:n-1]

    min_dfs = abs(sum(c1)-sum(c2))

    print(min_dfs)
