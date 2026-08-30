from math import ceil
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    if a == b:
        moves = 0
    else:
        m = max(a, b) - min(a, b)
        moves = ceil(ceil(m/2)/c)
        
    print(moves)
