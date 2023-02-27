N, X = map(int, input(">>").split())  # N : 정수 개수 , X : 비교숫자
integer = list(map(int, input().split()))

for i in range(N):
    if integer[i] < X:
        print(integer[i], end=" ")
