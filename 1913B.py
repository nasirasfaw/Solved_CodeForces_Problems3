t = int(input())
for _ in range(t):
    s = input()
    c1, c0 = s.count('1'), s.count('0')
    answer = 0
    for i in range(len(s)):
        if s[i] == '1':
            if c0 > 0:
                c0 -= 1
            else:
                answer = len(s) - i
                break
        else:
            if c1 > 0:
                c1 -= 1
            else:
                answer = len(s) - i
                break
    print(answer)
