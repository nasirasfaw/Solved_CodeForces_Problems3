t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k != 4:
        ans = min((k - x % k) % k for x in a)
        print(ans)

    else:
        ans1 = min((4 - x % 4) % 4 for x in a)

        even = sum(x % 2 == 0 for x in a)
        ans2 = max(0, 2 - even)

        print(min(ans1, ans2))
