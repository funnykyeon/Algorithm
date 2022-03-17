import sys
N, M = map(int, sys.stdin.readline().split())
# 첫째줄에 저장된 사이트주소의 수 N과  찾으려는 사이트주소의 수 M을 sys를 이용하여 빠르게 입력받습니다.(시간초과방지)

site_password = {}
# 파이썬은 해시테이블을 별도 구현할필요없이 딕셔너리타입을 사용하면 됩니다.
# 파이썬 해시테이블 구현방식은 오픈어드레싱 방식이며
# 충돌 발생시 탐사를 통해 빈공간을 찾아나서는 방식입니다.

for _ in range(N):
    site, password = sys.stdin.readline().split()
    site_password[site] = password
# key값으로 site를, value값으로 password를 딕셔너리 자료형으로 집어넣고

for _ in range(M):
    want_site = sys.stdin.readline().rstrip()
    print(site_password[want_site])
    # 키값에 비밀번호를 찾으려는 사이트의 주소가 들어오면 그에 맞는 value값을 반환

    # 요약
    # site password N개값 만큼 딕셔너리에 넣어주고
    # key값으로 value찾으면 끝14