
while True:
# 무한루프 while문
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    # a==0이거나 b==o 일때 break으로 무한루프 탈출
    print(a+b)