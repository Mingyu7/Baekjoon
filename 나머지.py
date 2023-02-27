N = []
for _ in range(10):
    N.append(int(input()))
for i in range(10):
    temp2 = 0
    temp = N[i] % 42
    temp2 += temp
print(temp2)
