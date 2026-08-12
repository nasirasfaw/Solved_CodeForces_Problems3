t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    
    if len(a) >= 2 and any((s-a[i]) % 2 == a[i] % 2 for i in range(len(a))):
        print("YES")
    else:
        print("NO")
