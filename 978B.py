n = int(input())
s = input()
s1 = []
i = 0
for j in range(1, len(s)):
    if s[j] != s[j-1]:
        s1.append(s[i:j])
        i = j
s1.append(s[i:])
count = 0
for i in range(len(s1)):
    if 'x' in s1[i] and len(s1[i]) > 2:
        count += len(s1[i]) - 2
              
print(count)
