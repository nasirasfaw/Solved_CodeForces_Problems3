t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    psum = 0
    pmax = 0
    for x in a:
        psum += x
        pmax = max(pmax, x)
        if psum == 2*pmax:
            count += 1

    print(count)
