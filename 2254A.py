t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    p = [a, b, c]
    p.sort()

    m1 = p[1] - p[0]
    m2 = p[2] - p[1]

    print(min(m1, m2))
