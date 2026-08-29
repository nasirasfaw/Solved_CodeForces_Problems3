t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())

    moves = {(a, b), (a, -b), (-a, b), (-a, -b),
             (b, a), (b, -a), (-b, a), (-b, -a)}

    king = set()
    queen = set()
    
    for x, y in moves:
        king.add((xk + x, yk + y))
        queen.add((xq + x, yq + y))

    common = king & queen

    print(len(common))
