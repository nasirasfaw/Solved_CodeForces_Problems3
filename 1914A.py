import string
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    st = {}
    for i, ch in enumerate(list(string.ascii_uppercase)):
        st[ch] = i+1

    st2 = set()

    for x in s:
        if s.count(x) >= st[x]:
            st2.add((x, st[x]))

    print(len(st2))
