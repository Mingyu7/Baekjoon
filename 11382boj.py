n = input().split()
a =int(n[0])
b=int(n[1])
c=int(n[2])
print(a+b+c)
#map 함수 사용하면 간단
print(sum(map(int, input().split())))
# 입력 받아서 int형으로 변환을하고 sum해서 바로 출력