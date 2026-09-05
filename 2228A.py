t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    c0, c1, c2 = w.count(0), w.count(1), w.count(2)
    
    d = abs(c1-c2)
    
    if c1 < c2:
        answer = c0 + c1+ d//3
    else:
        answer = c0 + c2 + d//3

    print(answer)
