N, M = map(int, input().split())
basket = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):  # 1 ~ M 번째 까지 바구니에 번호 넣기
        basket[n] = k

for i in range(1, N+1):  # 바구니 개수만큼 출력
    print(basket[i], end=' ')
