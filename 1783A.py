t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    if a[0] == a[-1]:
        print("NO")
    else:
        print("YES")
        b = a[1:]
        b.sort(reverse=True)
        c = [a[0]] + b
        print(*c)
