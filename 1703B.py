t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    total = 0
    for x in set(s):
        total += s.count(x) + 1
    print(total)
