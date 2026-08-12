n = int(input())

data_base = {}
for i in range(n):
    name = input()
    if name not in data_base:
        print("OK")
        data_base[name] = 1
    else:
        print(name + str(data_base[name]))
        data_base[name] += 1
