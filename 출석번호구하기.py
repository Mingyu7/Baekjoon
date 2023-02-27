N = []
chk = [i for i in range(1, 31)]
for i in range(28):
    N = int(input())
    chk.remove(N)  # 지우기
print(min(chk))
print(max(chk))
