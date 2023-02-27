N = int(input())  # 정수의 개수
integer = list(map(int, input().split()))
V = int(input())  # 찾으려는 정수
count = 0

for i in range(N):
    print(integer[i])
    if V == integer[i]:
        count += 1
print(count)
