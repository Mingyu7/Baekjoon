N, M = map(int, input().split())
ballbox = [] * [N]

# M 번째의 공

for _ in range(M):
    i, j, K = map(int, input().split())
    for i in range(i, j+1):  # 1! M 번째 까지 바구니에 번호 넣기
        ballbox[i] = k  # 숫자 넣기
for i in range(1, N+1)  # 바구니 개수만큼 출력
print(ballbox[i], end=" ")


# N, M = map(int, input().split())


# def BallBox():
#     N, M = map(int, input().split())
#     basket = [0] * (N+1)

#     for _ in range(M):
#         i, j, k = map(int, input().split())
#         for n in range(i, j+1):
#             basket[n] = k

#     for i in range(1, N+1):
#         print(basket[i], end=' ')
