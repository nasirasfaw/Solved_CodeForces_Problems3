from math import ceil
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    maxm = max(n, m)
    minm = min(n, m)
    if maxm % 2 != 0:
        print(minm * (maxm-1)//2 + ceil(minm/2))
    else:
        print(minm * maxm//2)
