li = ["0101", "1000"]
a, b = list(li[0]), list(li[1])
res = []
for i in range(len(a)):
    if a[i] == "1" and b[i] == "0":
        x = "1"
    elif a[i] == "0" and b[i] == "0":
        x = "0"
    else:
        x = "0"
    res.append(x)
print(''.join(res))

li = ["10101", "11010"]
a, b = list(li[0]), list(li[1])
res = []
print(range(len(a)))
for i in range(len(a)):
    print(i)
    if a[i] == "0" and b[i] == "0":
        x = "0"
    if a[i] == "1" and b[i] == "0":
        x = "1"
    else:
        x = "0"
    res.append(x)
print("".join(res))
