t = int(input())
for _ in range(t):
    n = int(input())
    
    k = n//2
    moves = 0
    while k > 0:
        moves += (4*n-4)*k
        n -= 2
        k -= 1

    print(moves)
