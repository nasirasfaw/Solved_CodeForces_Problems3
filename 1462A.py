t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    a = []
    i = 0
    j = n-1
    while i < j:
        a.append(b[i])
        a.append(b[j])
        i += 1
        j -= 1
    if n % 2 == 1:
        a.append(b[n//2])

    print(*a)
