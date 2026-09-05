t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    possible = True
    for i in range(n - 2, -1, -1):
        if a[i] >= a[i + 1]:
            if a[i+1] == 0:
                possible = False
                break

            k = a[i].bit_length() - a[i+1].bit_length()
            if (a[i] >> k) >= a[i + 1]:
                k += 1
            a[i] >>= k
            ans += k
    if possible:
        print(ans)
    else:
        print(-1)
