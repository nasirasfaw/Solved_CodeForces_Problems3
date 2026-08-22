n = int(input())
s = input()

s1 = []
i = 0
d = 1    #d = length
while i < len(s):
    s1.append(s[i:i+d])
    i += d
    d += 1

answer = ""
for x in s1:
    answer += x[0]
    
print(answer)
