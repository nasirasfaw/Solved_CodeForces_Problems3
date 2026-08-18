n = int(input())
n = str(n)
ok = True
if n[0] == '4' or n[:2] == '44':
    ok = False
ok1 = (set(n) == {'1', '4'}) or set(n) == {'1'}
n1 = []
i = 0
for j in range(len(n)):
    if n[j] != n[j-1]:
        n1.append(n[i:j])
        i = j
n1.append(n[i:])

ok2 = True
for x in n1:
    if '4' in x and len(x) > 2:
        ok2 = False
print("YES" if ok and ok1 and ok2 else "NO")
