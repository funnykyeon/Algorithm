import sys
# stdin.readline 함수를 사용하려면 먼저 sys 모듈을 불러들여야 한다.
# 모듈을 불러들일 때는 import 구문을 이용해서 작성한다. 보통 import 구문은 코드 맨 윗줄에 작성한다.
t = int(sys.stdin.readline())
# sys 모듈을 불러들였으니 sys.stdin.readline() 함수를 사용한다.
# 사용 방식과 기능은 input 함수를 사용할 때와 동일하다.
# 입력받는 문자는 사용자가 숫자를 입력하더라도 문자열로 입력받게 된다.
# 그래서 int 함수를 이용해서 입력받은 문자를 정수로 변환하였다.
for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    # 동일하게 sys.stdin.readline() 함수를 사용한다
    print(a+b)
