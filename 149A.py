k = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
if k == 0:
    print(0)
else:
    for i in range(12):
        if sum(a[:i+1]) >= k:
            print(i+1)
            break
    else:
        print(-1)
