n = int(input('실행할 횟수 : '))
stack= []

for i in range(n):
    com = input().split()

    if com[0] == 'push': # 스택에 숫자 넣기
        stack.append(com[1])
    elif com[0] == 'pop': #가장 위에있는 숫자 빼기
        if len(stack) == 0: #스택에 아무것도 없으면 -1 출력
            print(-1)
        else:
            print(stack.pop()) #그렇지 않으면 맨위 숫자 빼기
    elif com[0] == 'size': # stack의 size 출력
        print(len(stack))
    elif com[0] == 'empty': #stack이 비어있으면 1 , 그렇지 않으면 0
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'top': # stack의 맨위 숫자 출력
        if len(stack) == 0: # stack 비어있으면 -1 출력
            print(-1)
        else:
            print(stack[-1]) # stack 0 번째 숫자 출력
