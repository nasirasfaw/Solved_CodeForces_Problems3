t = int(input())
for _ in range(t):
    n = int(input())

    p = list(range(1, n+1))

    p1 = p[1:] + [p[0]]

    print(*p1)
