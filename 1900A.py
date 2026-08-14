t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    s1 = []
    i = 0
    for j in range(1, n):
        if s[j] != s[j-1]:
            s1.append(s[i:j])
            i = j
    s1.append(s[i:])
    if '.' not in s:
        answer = 0
    else:
        if any('.' in x and len(x) >= 3 for x in s1):
            answer = 2
        else:
            answer = s.count('.')
    print(answer)
