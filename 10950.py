t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    # map(적용할 함수, 순회 가능한 객체)
    print(a+b)