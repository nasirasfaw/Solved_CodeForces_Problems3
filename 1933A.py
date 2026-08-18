t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a = [abs(x) for x in a]

    print(sum(a))
