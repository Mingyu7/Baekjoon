import sys
T = int(sys.stdin.readline())  # 반복 횟수
T1 = []
for i in range(T):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(n1 + n2)
