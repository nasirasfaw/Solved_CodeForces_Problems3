t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    diam = abs(a - b)
    
    n = 2 * diam

    if max(a, b, c) > n:
        print(-1)
    else:
        if c <= diam:
            print(c + diam)
        else:
            print(c - diam)
