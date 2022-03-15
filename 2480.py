import sys
input=sys.stdin.readline()
# A = 1
# B = 9
# C = 6

A, B, C = map(int,input().split())

# 같은눈이 3개 나오면 10,000원+(같은 눈)×1,000
# 같은눈이 2개 나오면 1,000원+(같은 눈)×100원
# 모두 다른눈이 나오면  (그 중 가장 큰 눈)×100원
if A==B==C :
    print(10000+1000*A)
elif A==B :
    print(1000+100*A)
elif B==C :
    print(1000+100*B)
elif A==C :
    print(1000+100*A)

elif A!=B and B!=C or A!=C :
    M = max(A,B,C)
    # max를 써 큰수를 가져온다
    print(M*100)