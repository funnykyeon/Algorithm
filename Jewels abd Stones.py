J = "aA"
S = "aAAbbbb"
# 원하는출력 3

freqs = {}
count = 0
#돌(S)의 빈도 수 계산
for char in S:
    if char not in freqs:
        freqs[char] = 1
    else:
        freqs[char] += 1
# 보석(j)의 빈도수 계산
for char in J:
    if char in freqs:
        count += freqs[char]
        # count로 freqs[char]에 숫자 1,2를 합산
print(count)