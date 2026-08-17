t = int(input())
for _ in range(t):
    n = input()
    
    n = str(n)
    p = "3141592653589793238462643383279"
    count = 0
    for i in range(len(n)):
        if n[i] == p[i]:
            count += 1
        else:
            break
            
    print(count)
