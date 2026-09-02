t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    kr = max(n-k, n-(n-k))
    k1, k2 = s[:k], s[kr:]

    left = k1.count("L") 
    right = k2.count("R")
    
    answer = left + right

    if len(k1) == len(k2):
        print(answer)
    else:
        print(-1)
