a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
# count함수를 사용하기위해선 int가 아닌 str로 변환해줘야 사용가능하다
for i in range(10):
    # 0~9까지 사용된 숫자를 찾기위에 for문을 돌린다
    print(result.count(str(i)))