from sys import stdin

N = int(stdin.readline())
Que = []
for i in range(N):
    A = stdin.readline().split() # push 명령어 입력시 공백으로 split 구분 후 뒤에 정수만 넣기 위함

    if A[0] == 'push':
        Que.append(A[1])

    elif A[0] == 'pop':
        if Que:
            # deque에서 pop할땐  popleft()를 사용해야함
            print(Que.pop(0))
        else:
            print(-1)

    elif A[0] == 'size':
        # len으로 Que개수 확인
        print(len(Que))

    elif A[0] == 'empty':
        if len(Que) == 0:
            print(1)
        else:
            print(0)

    elif A[0] == 'front':
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[0])
    #       Que가 비어있지않다면 Que에 0번째(front) 출력

    elif A[0] == 'back':
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[-1])