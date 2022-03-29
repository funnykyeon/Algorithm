a = []
for i in range(9):
    a.append(int(input()))
# a라는 빈리스트를 정의하고 반복문을 통해 입력을 받는다.
print(max(a))
print(a.index(max(a))+1)
# 최대값 자리를 구하기위해 index함수를 사용하는데 예제 입력에서는 첫시작이 1부터 시작하여 8을 출력한다
# 파이썬에서는 0부터 시작하기에 index에 1을 더해 출력한다!