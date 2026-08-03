t = int(input())
for _ in range(t):
    n = int(input())

    n1 = [d for d in str(n)]
    
    if n <= 8:
        answer = 0
    elif n == 9:
        answer = 1
    elif n1[-1] == '9':
        answer = int("".join(n1[:len(n1)-1])) + 1
    else:
        answer = int("".join(n1[:len(n1)-1]))

    print(answer)
