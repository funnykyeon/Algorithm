#pypy3 로 재출
import sys
v, e = map(int, sys.stdin.readline().split())
inf = 100000000
s = [[inf] * v for i in range(v)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    s[a - 1][b - 1] = c
for k in range(v):
    for i in range(v):
        for j in range(v):
            if s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]
result = inf
for i in range(v):
    result = min(result, s[i][i])
if result == inf:
    print(-1)
else:
    print(result)