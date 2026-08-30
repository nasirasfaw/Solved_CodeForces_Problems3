t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())

    x, y, z = b, c, d

    if b + c > d:
        print(b, c, d)
    else:
        print(b, c, c)
