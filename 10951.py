import sys

while True:
	try:
		a,b=map(int,sys.stdin.readline().split())
	except:
        # 오류입력
		break
	print(a+b)