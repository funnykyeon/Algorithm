
a = [4, 6, 2, 9, 1]
# 최대값을 구하는 알고리즘을 len(a) -1 만큼 반복한다
iters = len(a) - 1
# 반복횟수는 버블과 동일
for iter in range(iters):
#iter=반복회차
    minimun = iter #첫번째 시도에선 0
    for cur in range(iter +1, len(a)):
        # 1~제일마지막자리4까지  cur이 반복
        if a[cur] < a[minimun]:
        #처음 cur은 1이니 첫번째 녀석과 < 0번째녀석 비교
        #횟수마다 cur은 2,3,4
            # cur이 작다면 아래래 f문을 태운다
            minimun = cur
        #  for문의 cur을 전부 돌렸을때 minimun에 제일 작은수가 들어있다
        # 최소의 위치를 찾은후

        # 검증후 최소값 자리이동동
        if minimun != iter:
            # 최소의위치 != 처음0
            a[minimun], a[iter] = a[iter], a[minimun]
            print(a)
