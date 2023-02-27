N, M = map(int, input().split())
ballbox = [i for i in range(1, N + 1)]  # 1~N 까지 숫자 순서대로 넣기
for b in range(M):
    i, j = map(int, input().split())
    box = ballbox[i-1]
    ballbox[i-1] = ballbox[j-1]
    ballbox[j-1] = box
print(ballbox)
