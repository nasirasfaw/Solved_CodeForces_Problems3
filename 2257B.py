t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
        
    if a[0] + n - 1 >= b[0] + m - 1:
        print(1)
    else:
        print(2)
