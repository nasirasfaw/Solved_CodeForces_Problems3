key = "qwertyuiopasdfghjkl;zxcvbnm,./"
direction = input()
message = input()

original = ""

for ch in message:
    k = key.index(ch)
    if direction == 'R':
        original += key[k-1]
    else:
        original += key[k+1]

print(original)
