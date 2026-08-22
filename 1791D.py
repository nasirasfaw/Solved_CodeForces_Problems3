t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    ss = list(set(s))
    sl = [0]
    for x in ss:
        if s.count(x) >= 2:
            sl.append(len(set(s[:s.index(x)+1])) + len(set(s[s.index(x)+1:])))

    print(max(len(ss), max(sl)))
