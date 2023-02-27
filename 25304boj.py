money = int(input())  # 총금액
number = int(input())  # 물건의 종류의 수
sum = 0

for i in range(1, number+1):
    price, count = map(int, input().split())  # 각물건의 가격  개수
    sum += price * count  # 500

if sum == money:
    print('Yes')
else:
    print("No")
