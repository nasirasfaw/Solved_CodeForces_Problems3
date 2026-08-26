t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    m = min(abs(x), abs(y))

    if x == 0 and y == 0:
        price = 0
    elif (abs(x) > 0 and y == 0) or (x == 0 and abs(y) > 0):
        price = max(abs(x), abs(y))*a
    elif (x > 0 and y > 0) or (x < 0 and y < 0):
        price = min(m*b, 2*m*a) + abs(x-y)*a 
    elif (x < 0 and y > 0) or (x > 0 and y < 0):
        price = abs(x-y)*a

    print(price)
