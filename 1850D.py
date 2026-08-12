t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    s.sort()
    s1 = []
    i = 0
    for j in range(1, n):
        if s[j] - s[j-1] > k:
            s1.append(s[i:j])
            i = j
    s1.append(s[i:])
    mx = max(len(x) for x in s1)

    print(n - mx)
