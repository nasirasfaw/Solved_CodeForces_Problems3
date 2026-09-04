t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ap = [abs(x) for x in a]

    a1 = []
    for i in range(n):
        if a[i] < 0:
            a1.append(a[i])

    if len(a1) % 2 == 0:
        s = sum(ap)
    else:
        s = sum(ap) - 2*min(ap)

    print(s)
