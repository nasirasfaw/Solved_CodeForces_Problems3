t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    p = [a, b, c]
    p.sort()
    rge1 = p[2] - p[0]
    
    if p[0]+p[1] >= p[2]:
        print(rge1)
    else:
        p[2] = p[0] + p[1]
        rge2 = p[2] - p[0]
        print(rge2)
