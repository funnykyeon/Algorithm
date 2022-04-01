import os
import time
from datetime import datetime, timedelta

# 현재시간 기준 날짜
time2 = datetime.now()

for i in range(365):
    # 날짜 변수
    what_day = (time2 - timedelta(days=i)).strftime('%a %b %d %H:%M:%S %Y')

    # 텍스트파일 작성
    f = open("/Users/kiwon/PycharmProjects/kkk/bb.txt", 'w')
    f.write(f'{i}')
    f.close

    # 깃 프로세스 진행(깃 Add+Commit -> 날짜 수정 -> 깃 푸시)
    os.system(f'git commit -am "오토 깃 테스트{i}"')
    os.system(
        f'git commit --amend --no-edit --date "{what_day} +0900T"')
    os.system(f'git push origin main')

    print(f'{i + 1}회차 완료되었음')

