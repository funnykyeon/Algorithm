import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline()
# input보다 더빠르고 메모리도 적게 소모한다
# 입력받은 뒤 입력받은값 맨뒤 '\n'개행문자 포함된다

n,m = map(int, input().split())
d = {}
for _ in range(n):
    id, pwd = input().strip('\n').split()
    d[id] =pwd

for _ in range(m):
    id = input().strip('\n')
    print(d[id])