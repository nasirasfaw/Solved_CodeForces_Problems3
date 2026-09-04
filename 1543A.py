t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    d = abs(a - b)
    m1 = min(a, b)
    m2 = max(a, b)
    if a == b:
        print(0, 0)
    else:
        n = min(m2 % d, d - (m2 % d))
        print(d, n)
