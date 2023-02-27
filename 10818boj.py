N = int(input())
num = map(int, input().split())
min = num[0]
max = num[0]
for i in range(N):
    if max < num[i]:
        max = num[i]
    elif min > num[i]:
        min = num[i]

print(max, end=' '+min)

# cnt = int(input()) # 최대, 최소 값 구하기
# numbers = list(map(int, input().split()))
# print(min(numbers),max(numbers))
