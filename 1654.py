import sys

input = sys.stdin.readline

def f(mid):
    cnt = 0
    for i in range(len(a)):
        cnt += a[i] // mid
    return cnt


k, n = map(int, input().split())

a = []
for _ in range(k):
    a.append(int(input()))

left, right, ans = 0, max(a), 0
while left <= right:
    mid = (left + right) // 2
    if mid == 0:
        ans = 1
        break

    cnt = f(mid)
    if cnt >= n:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)