# 1000,1001,1002,1008 동일문제

# 방법1 (백준에서 예제입력 받는다)
# map(적용할 함수, 순회 가능한 객체)
# 순회 가능한 객체의 각 원소에 지정한 함수를 각각 적용하여
# 결과를 반환하는 함수
# int 함수를 5개의 객체에 각각 맵핑하여
# string 자료형도 int 자료형으로 바꿔주었고,
# float 자료형도 int 자료형으로 변환하면서 소수점 자리를 버림
A, B = map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
# 몫은 //
print(A%B)


# 방법2 (백준에서 예제입력 받는다)
# input 으로 문자열 받은후 split으로 공백제거
A, B = input().split()
print(int(A)+int(B))
# 문자열인 A,B를 int함수를 사용하여 숫자로 변형
print(A+B)
print(A-B)
print(A*B)
print(A//B)
# 몫은 //
print(A%B)