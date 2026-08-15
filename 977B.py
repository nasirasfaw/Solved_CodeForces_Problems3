n = int(input())
s = input()

s1 = []
for i in range(1, len(s)):
    s1.append(s[i-1:i+1])

mx = max(s1.count(x) for x in s1)

for i in range(len(s1)):
    if s1.count(s1[i]) == mx:
        print(s1[i])
        break
