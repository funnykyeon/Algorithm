# 첫째 줄에 저장된 사이트 주소의 수 N(1 ≤ N ≤ 100,000)과 비밀번호를 찾으려는 사이트 주소의 수 M(1 ≤ M ≤ 100,000)이 주어진다.
# 두번째 줄부터 N개의 줄에 걸쳐 각 줄에 사이트 주소와 비밀번호가 공백으로 구분되어 주어진다.
# 사이트 주소는 알파벳 소문자, 알파벳 대문자, 대시('-'), 마침표('.')로 이루어져 있고, 중복되지 않는다.
# 비밀번호는 알파벳 대문자로만 이루어져 있다.
# 모두 길이는 최대 20자이다.
# N+2번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한줄에 하나씩 입력된다.
# 이때, 반드시 이미 저장된 사이트 주소가 입력된다.


# 16 4
# noj.am IU
# acmicpc.net UAENA
# startlink.io THEKINGOD
# google.com ZEZE
# nate.com VOICEMAIL
# naver.com REDQUEEN
# daum.net MODERNTIMES
# utube.com BLACKOUT
# zum.com LASTFANTASY
# dreamwiz.com RAINDROP
# hanyang.ac.kr SOMEDAY
# dhlottery.co.kr BOO
# duksoo.hs.kr HAVANA
# hanyang-u.ms.kr OBLIVIATE
# yd.es.kr LOVEATTACK
# mcc.hanyang.ac.kr ADREAMER
# startlink.io
# acmicpc.net
# noj.am
# mcc.hanyang.ac.kr


import sys
# 첫째줄에 저장된 사이트주소의수N과 찾으려는 사이트주소의수 M을 sys를 이용하여 빠르게 입력받는다.
N, M = map(int, sys.stdin.readline().split())

site_password = {}
# 파이썬은 해쉬를 별도 구현할필요없이 딕셔너리타입을 사용하면 된다.
# 충돌시 오픈어드레싱이라는 것은 사용한다.(탐사후 빈공간 쇽속)

for _ in range(N):
    site, password = sys.stdin.readline().split()
    site_password[site] = password
#      key값으로 site를 value값으로 password를 넣어 딕셔너리를 만들어준다

for _ in range(M):
    want_site = sys.stdin.readline().rstrip()
    # N+2번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한줄에 하나씩 입력된다.
    print(site_password[want_site]) # 원하는 사이트(key)의 비밀번호(value) 출력


    # 요약 site password N개값 만큼 딕셔너리에 넣어주고
    #     key값으로 value찾으면 끝