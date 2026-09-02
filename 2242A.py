t = int(input())
for _ in range(t):
    k = int(input())
    c = list(map(int, input().split()))

    c.sort(reverse=True)
    if len(c) == 1:
        print("YES" if c[0] >= 3 else "NO")
    else:
        if c[0] >= 3 or (c[0] + c[1] >= 4):
            print("YES")
        else:
            print("NO")
