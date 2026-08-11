t = int(input())
for _ in range(t):
    x = int(input())

    y = []
    for i in range(1, 10):
        y += [i, 10*i+i, 100*i+10*i+i, 1000*i+100*i+10*i+i]
                
    for k in range(len(y)):
        if y[k] == x:
            yx = y[:k+1]
    answer = 0
    for r in yx:
        r1 = [int(d) for d in str(r)]
        answer += len(r1)

    print(answer)
