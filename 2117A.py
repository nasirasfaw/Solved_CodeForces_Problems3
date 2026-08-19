t = int(input())
for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))

        k1 = a.index(1)
        k2 = a[::-1].index(1)

        if x >= len(a[k1:n-k2]):
                print("YES")
        else:
                print("NO")
