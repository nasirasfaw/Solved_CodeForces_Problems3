t = int(input())
for _ in range(t):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))

    af = a[f-1]
    cf = a.count(af)
    a.sort(reverse=True)
    afi = a.index(af)
    
    if k < afi+1:
        print("NO")
    elif k < afi + cf:
        print("MAYBE")
    else:
        print("YES")
