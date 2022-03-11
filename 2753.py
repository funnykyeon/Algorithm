# 예시)
# year = 501
# #  예시 year(501)/4를 할경우 몫은 125
# #                      나머지는 1
# if ((year%4 == 0)and(year%100 != 0)or(year%400 == 0)):
#     # 0과 같다면 정확한배수
#     print('uuuu')
# else:
#     print('xxxxx')


year = int(input())
if ((year%4 == 0)and(year%100 != 0)or(year%400 == 0)):
    print('1')
else:
    print('0')