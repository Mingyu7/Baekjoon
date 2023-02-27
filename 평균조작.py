N = int(input())
temp = 0
score = list(map(int, input().split()))
M = max(score)
for i in range(N):
    newscore = score[i]/M*100
    temp += newscore
print(temp/N)
