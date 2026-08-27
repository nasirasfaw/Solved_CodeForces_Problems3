t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    m = min(a)
    sum = 0
    for i in range(n):
        sum += a[i]-m
    
    print(sum)
