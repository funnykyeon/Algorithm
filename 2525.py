# A, B = map(int, input().split())
# C = int(input())
A=23
B=48
C=25


A = (A + ((B + C)//60)) % 24
# 나머지로 풀어보았습니다.
B = (B + C) % 60
print(A)

#
# hour=23
# minute=48
# add=25