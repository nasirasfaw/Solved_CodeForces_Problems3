t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ab = []
    for i in range(n):
        ab.append([b[i], a[i]])
    ab.sort()
    cost = p
    n_people = 1
    i = 0
    while n_people < n:
        cost += min(ab[i][0], p)*ab[i][1]
        n_people += ab[i][1]
        i += 1
        if n_people > n:
            cost -= (n_people - n) * min(ab[i-1][0], p)
    print(cost)
