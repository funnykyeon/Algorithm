# 첫째줄에 N과X 주어진다 <=10000
# 정수 N개로 이루어진 수열 A

# 정수 X

N, X = map(int, input().split())
A = list(map(int, input().split()))


for i in range(N):
    if A[i] < X:
     print(A[i],end=" ")