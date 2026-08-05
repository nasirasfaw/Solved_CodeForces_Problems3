t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    avg = sum(a) // n

    current = 0
    ok = True
    for x in a:
        current += x - avg
        if current < 0:
            ok = False
            break

    print("YES" if ok else "NO")
