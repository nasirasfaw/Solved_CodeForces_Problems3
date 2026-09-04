t = int(input())
for _ in range(t):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))

    sa = sum(a)

    if sa <= s and (s - sa) % x == 0:
        print("YES")
    else:
        print("NO")
