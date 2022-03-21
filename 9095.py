# 1,2,3 더하기
T = int(input())

result = []

def back(num, sum):
    global count
    if num<sum:
        return
    if num==sum:
        count +=1
        return
    for i in range(1, 4):
        sum +=i
        back(num,sum)
        sum -= i

for _ in range(T):
    num = int(input())
    count = 0
    back(num, 0)
    result.append(count)
for answer in result:
    print(answer)
